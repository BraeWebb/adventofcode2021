theory parsing
  imports Main
  keywords
    "load" :: thy_decl and
    "load_file" :: thy_load and
    "snipbegin" :: document_heading and
    "snipend" :: document_heading
begin

ML \<open>
fun symbols_to_lines (start:string) (symbols:Symbol_Pos.T list) =
  case symbols of
    [] => [] |
    (("\n", _) :: xs) => start :: symbols_to_lines "" xs |
    ((chr, _) :: xs) => symbols_to_lines (start ^ chr) xs

fun read_lines (source: Input.source) =
  filter (fn line => line <> "") (symbols_to_lines "" (Input.source_explode source))

fun list_to_string (xs: string list) =
  case xs of [] => "]" |
       (x :: []) => (("''" ^ x ^ "'']")) |
       (x :: xs) => (("''" ^ x ^ "'', ") ^ (list_to_string xs))

fun record_definition (name: binding) (lines: string list) thy =
  let
    val trm = "[" ^ (list_to_string lines);
    val _ = @{print} trm;
    val t = Syntax.read_term thy trm;
    val ((_, (_, def)), lthy') = Local_Theory.define ((name, NoSyn), ((Thm.def_binding name, []), t)) thy;
    val lthy'' = Code.declare_default_eqns [(def, true)] lthy';
  in
    lthy''
  end

fun parse (name: binding, source:Input.source) =
   record_definition name (read_lines source)

val _ = Outer_Syntax.local_theory \<^command_keyword>\<open>load\<close>
    "load an inline file as a list of string"
   (Parse.binding -- Parse.document_source >> parse)

fun parse_file (name, files:(theory -> Token.file)) thy =
  let
    (*val thy = Toplevel.theory_of state;*)
    val lines = #lines (files thy);
    val _ = @{print} lines;
    (*val thy' = record_definition name lines @{context}*)
  in
    thy
  end

val _ = Outer_Syntax.command \<^command_keyword>\<open>load_file\<close>
    "load a file as a list of string"
   (Parse.binding -- Resources.parse_file
     >> (Toplevel.theory o parse_file))
\<close>

load mylines \<open>
oh fuck yeah
hello world!
\<close>

value mylines
 
(*load_file morelines "day1.in"*)

section Snipping

ML \<open>
fun wrapped_command (command: string) (name: string option) =
  let
    val command = "\\" ^ command
    val argument = case name of 
      NONE => "" |
      SOME v => ("{" ^ v ^ "}")
    val doc = Input.string (command ^ argument)
  in
    (Pure_Syn.document_command {markdown = false} (NONE, doc))
  end

val _ =
  Outer_Syntax.command ("snipbegin", \<^here>) "start a snippet"
    (Parse.name >> (fn n => wrapped_command "isamarkupsnipbegin" (SOME n)));

val _ =
  Outer_Syntax.command ("snipend", \<^here>) "finish a snippet"
    (Parse.document_source >> (fn _ => wrapped_command "isamarkupsnipend" (NONE)));
\<close>

snipbegin hello

text \<open>Hello world! @{value mylines}\<close>

snipend -

end