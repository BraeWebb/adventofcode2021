section "Day 1: Sonar Sweep"
theory day1
imports Main "HOL-Library.FSet"
begin

text "
You're minding your own business on a ship at sea when the overboard alarm goes off!
You rush to see if you can help.
Apparently, one of the Elves tripped and accidentally sent the sleigh keys flying into the ocean!

Before you know it, you're inside a submarine the Elves keep ready for situations like this.
It's covered in Christmas lights (because of course it is),
and it even has an experimental antenna that should be able to track the keys if you can boost its signal strength high enough;
there's a little meter that indicates the antenna's signal strength by displaying 0-50 stars.

As the submarine drops below the surface of the ocean,
it automatically performs a sonar sweep of the nearby sea floor.
On a small screen, the sonar sweep report (your puzzle input) appears:
each line is a measurement of the sea floor depth as the sweep looks further and further away from the submarine.
"

text "For example, suppose you had the following report:"

definition example1 :: "nat list" where
  "example1 = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]"

text "@{value example1}"

text_raw "\\begin{verbatim}
199
200
208
210
200
207
240
269
260
263
\\end{verbatim}"

text "This report indicates that, scanning outward from the submarine,
the sonar sweep found depths of 199, 200, 208, 210, and so on."

subsection "Part One"
text "The first order of business is to figure out how quickly the depth increases,
just so you know what you're dealing with
- you never know if the keys will get carried into deeper water by an ocean current or a fish or something.
"

text "To do this, count the number of times a depth measurement increases from the previous measurement.
(There is no measurement before the first measurement.)
In the example above, the changes are as follows:"

text_raw "\\begin{verbatim}
199 (N/A - no previous measurement)
200 (increased)
208 (increased)
210 (increased)
200 (decreased)
207 (increased)
240 (increased)
269 (increased)
260 (decreased)
263 (increased)
\\end{verbatim}"

fun count_increases :: "('a::ord) list \<Rightarrow> nat" where
  "count_increases (x # y # xs) = (if x < y then 1 else 0) + count_increases (y # xs)" |
  "count_increases _ = 0"

text "In this example, there are @{value \<open>count_increases example1\<close>} measurements that are longer than the previous measurement."
value "count_increases example1"

lemma lt_2_imp_0: "size xs < 2 \<Longrightarrow> count_increases xs = 0"
  using count_increases.simps(2,3)
  by (metis length_0_conv length_Suc_conv less_2_cases)

lemma lt_2_imp_0_spec: "size xs < 2 \<Longrightarrow> card {i \<in> {0..<size xs - 1} . (xs!i < xs!(i+1))} = 0"
  by (induction xs; auto) 

value "{0::nat..<3}"

value "count_increases [1::nat]"

theorem
  assumes "n = card {i \<in> {0..<size xs - 1} . (xs!i < xs!(i+1))}"
  shows "count_increases xs = n"
  using assms apply (cases xs)
  apply simp
  apply (cases "size xs < 2")
   apply (simp add: lt_2_imp_0) unfolding count_increases.simps
  sorry

subsection "Part Two"
text "Considering every single measurement isn't as useful as you expected:
there's just too much noise in the data.

Instead, consider sums of a three-measurement sliding window.
Again considering the above example:"

text_raw "\\begin{verbatim}
199  A      
200  A B    
208  A B C  
210    B C D
200  E   C D
207  E F   D
240  E F G  
269    F G H
260      G H
263        H
\\end{verbatim}"

text "Start by comparing the first and second three-measurement windows.
The measurements in the first window are marked A (199, 200, 208);
their sum is 199 + 200 + 208 = 607.
The second window is marked B (200, 208, 210);
its sum is 618.
The sum of measurements in the second window is larger than the sum of the first,
so this first comparison increased.

Your goal now is to count the number of times the sum of measurements in this sliding window increases from the previous sum.
So, compare A with B, then compare B with C, then C with D, and so on.
Stop when there aren't enough measurements left to create a new three-measurement sum.

In the above example, the sum of each three-measurement window is as follows:"

text_raw "\\begin{verbatim}
A: 607 (N/A - no previous sum)
B: 618 (increased)
C: 618 (no change)
D: 617 (decreased)
E: 647 (increased)
F: 716 (increased)
G: 769 (increased)
H: 792 (increased)
\\end{verbatim}"

fun windows :: "'a list \<Rightarrow> nat \<Rightarrow> ('a list) list" where
  "windows [] gap = []" |
  "windows xs gap = (if size xs \<ge> gap then take gap xs # windows (tl xs) gap else [])"

lemma "xs \<in> set (windows xss n) \<Longrightarrow> size xs = n"
  by (induction xss; auto)

lemma "windows example1 3 = [[199, 200, 208], [200, 208, 210], [208, 210, 200], [210, 200, 207], [200, 207, 240],
  [207, 240, 269], [240, 269, 260], [269, 260, 263]]"
  by eval  

fun sum_increases :: "(nat list) list \<Rightarrow> nat" where
  "sum_increases (x # y # xs) = (if sum_list x < sum_list y then 1 else 0) + sum_increases (y # xs)" |
  "sum_increases _ = 0"

text "In this example, there are @{value \<open>sum_increases (windows example1 2)\<close>} sums that are larger than the previous sum."
value "sum_increases (windows example1 3)"

end