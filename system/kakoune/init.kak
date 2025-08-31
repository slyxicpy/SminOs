set-option global tabstop 4
set-option global indentwidth 0
set-option global scrolloff 8,3
set-option global ui_options ncurses_enable_mouse=true
set-option global autocomplete insert|prompt
set-option global aligntab false
set-option global BOM none
set-option global eolformat lf
set-option global incsearch true
set-option global writemethod replace

map global insert <tab> '<ret>'
map global insert <s-tab> <c-p>

hook global InsertCompletionShow .* %{
    map global insert <up> <c-p> -docstring 'select previous completion'
    map global insert <down> <c-n> -docstring 'select next completion'
}
hook global InsertCompletionHide .* %{
    unmap global insert <up> <c-p>
    unmap global insert <down> <c-n>
}

hook global ModeChange push:.:insert %{
    set-face global PrimaryCursor rgb:000000,rgb:00ffff+b
}
hook global ModeChange pop:insert:. %{
    set-face global PrimaryCursor default,default
}

add-highlighter global/ show-matching
add-highlighter global/ wrap -word -width 120
add-highlighter global/ number-lines -hlcursor -separator ' ' -min-digits 3
add-highlighter global/ show-whitespaces -tab "▏" -tabpad " " -spc " " -lf " " -nbsp " "

define-command archivos %{
    info -title "ARCHIVOS COMUNES" "
Para abrir archivos usa: :edit NOMBRE

Ejemplos:
  :edit main.py
  :edit index.js
  :edit main.c
  :edit README.md
  :edit config.txt

O usa Tab para autocompletar nombres de archivos
"
}

define-command ayuda %{
    info -title "COMANDOS KAKOUNE" "
BASICOS:
  edit ARCHIVO  - Abrir archivo (:e ARCHIVO)
  write         - Guardar (:w)
  quit          - Salir (:q)
  quit!         - Salir sin guardar (:q!)

BUFFERS:
  buffer-next   - Siguiente archivo (:bn)
  buffer-previous - Archivo anterior (:bp)
  delete-buffer - Cerrar archivo actual (:db)

UTILIDADES:
  archivos      - Lista de archivos comunes
  ayuda         - Esta ayuda
  notas         - Crear archivo de notas nuevo
  debugeo       - Abrir depurador de errores (Python)

ATAJOS:
  Ctrl+S        - Guardar
  Ctrl+Q        - Salir
  Ctrl+N        - Siguiente buffer
  Ctrl+P        - Buffer anterior
  Alt+H         - Ayuda
  Alt+A         - Lista archivos
  Alt+N         - Crear notas
  Alt+D         - Depurador
"
}

define-command notas %{
    nop %sh{
        notesfile="notas.md"
        timestamp=$(date +"%Y-%m-%d %H:%M:%S")
        timed=$(echo "$timestamp" | sed 's/ /<space>/g')
        insert_keys="#<space>Notas<space>-<space>$timed<ret><ret>-"
        cmd="edit '$notesfile'; execute-keys ge a <ret> <ret> $insert_keys <esc>"
        tmux split-window -v -l 10 "kak -c '$kak_session' -e \"$cmd\""
    }
}
alias global notes notas

define-command debugeo %{
    nop %sh{
        errorfile="/tmp/kak_${kak_session}_errors.txt"
        touch "$errorfile"
        echo "No syntax errors." > "$errorfile"
        tmux split-window -h -b -l 30 "kak -c '$kak_session' -e \"rename-client debug; edit '$errorfile'; set-option buffer readonly true\""; tmux select-pane -R
    }
}

map global normal <c-s> ':write<ret>'
map global normal <c-q> ':quit<ret>'
map global normal <c-n> ':buffer-next<ret>'
map global normal <c-p> ':buffer-previous<ret>'
map global normal <c-w> ':delete-buffer<ret>'
map global normal <a-h> ':ayuda<ret>'
map global normal <a-a> ':archivos<ret>'
map global normal <a-n> ':notas<ret>'
map global normal <a-d> ':debugeo<ret>'

add-highlighter global/ regex '\b(TODO|FIXME|NOTE|BUG)\b' 0:comment
add-highlighter global/ regex '\b[0-9]+\b' 0:value
add-highlighter global/ regex '"[^"]*"' 0:string
add-highlighter global/ regex "'[^']*'" 0:string

hook global WinSetOption filetype=python %{
    try %{
        add-highlighter window/python-kw regex '\b(def|class|if|else|elif|for|while|try|except|finally|with|return|break|continue|pass|lambda|import|from|as)\b' 0:keyword
        add-highlighter window/python-fn regex '\b(print|len|range|str|int|float|list|dict|set|tuple|open)\b' 0:function
        add-highlighter window/python-comment regex '#.*$' 0:comment
    } catch %{}
    hook window BufWritePost .* %{
        nop %sh{
            errorfile="/tmp/kak_${kak_session}_errors.txt"
            python3 -m py_compile "$kak_buffile" > "$errorfile" 2>&1
            if [ ! -s "$errorfile" ]; then
                echo "No syntax errors." > "$errorfile"
            fi
        }
        evaluate-commands -try-client debug %{
            edit!
        }
    }
}

hook global WinSetOption filetype=c %{
    add-highlighter window/c regex '\b(int|char|float|double|void|if|else|for|while|do|switch|case|return|struct|typedef|include|define)\b' 0:keyword
    add-highlighter window/c regex '\b(printf|scanf|malloc|free|sizeof|NULL)\b' 0:function
    add-highlighter window/c regex '//.*$' 0:comment
}

hook global WinSetOption filetype=javascript %{
    add-highlighter window/js regex '\b(function|var|let|const|if|else|for|while|return|class|async|await|import|export)\b' 0:keyword
    add-highlighter window/js regex '\b(console|document|window|Array|Object|JSON)\b' 0:function
    add-highlighter window/js regex '//.*$' 0:comment
}

hook global WinSetOption filetype=go %{
    add-highlighter window/go regex '\b(func|if|else|for|range|switch|case|break|continue|return|struct|interface|type|package|import|const|var|defer|go)\b' 0:keyword
    add-highlighter window/go regex '\b(fmt|os|strings|time|errors|log|context)\b' 0:function
    add-highlighter window/go regex '//.*$' 0:comment
}

hook global WinSetOption filetype=ruby %{
    add-highlighter window/ruby regex '\b(def|class|module|if|else|elsif|for|while|until|case|when|break|next|return|require|include)\b' 0:keyword
    add-highlighter window/ruby regex '\b(puts|print|Array|Hash|String|Integer|File)\b' 0:function
    add-highlighter window/ruby regex '#.*$' 0:comment
}

hook global WinSetOption filetype=java %{
    add-highlighter window/java regex '\b(class|interface|if|else|for|while|do|switch|case|break|continue|return|public|private|protected|static|final|void|int|double|float|char|String)\b' 0:keyword
    add-highlighter window/java regex '\b(System|Math|Arrays|Collections|Objects)\b' 0:function
    add-highlighter window/java regex '//.*$' 0:comment
}

hook global WinSetOption filetype=rust %{
    add-highlighter window/rust regex '\b(fn|let|mut|if|else|for|while|loop|match|break|continue|return|struct|enum|impl|trait|use|mod)\b' 0:keyword
    add-highlighter window/rust regex '\b(String|Vec|Option|Result|Box|println)\b' 0:function
    add-highlighter window/rust regex '//.*$' 0:comment
}

hook global WinSetOption filetype=typescript %{
    add-highlighter window/typescript regex '\b(function|let|const|var|if|else|for|while|return|class|interface|type|async|await|import|export)\b' 0:keyword
    add-highlighter window/typescript regex '\b(console|Promise|Array|Object|Map|Set)\b' 0:function
    add-highlighter window/typescript regex '//.*$' 0:comment
}

hook global WinSetOption filetype=sh %{
    add-highlighter window/sh regex '\b(if|else|elif|fi|for|while|do|done|case|esac|break|continue|return|function|export|local)\b' 0:keyword
    add-highlighter window/sh regex '\b(echo|read|test|eval|source|set)\b' 0:function
    add-highlighter window/sh regex '#.*$' 0:comment
}

hook global WinSetOption filetype=cpp %{
    add-highlighter window/cpp regex '\b(int|char|float|double|void|if|else|for|while|do|switch|case|return|class|struct|template|namespace|using|public|private|protected)\b' 0:keyword
    add-highlighter window/cpp regex '\b(cout|cin|endl|string|vector|map|set)\b' 0:function
    add-highlighter window/cpp regex '//.*$' 0:comment
}

hook global WinSetOption filetype=cs %{
    add-highlighter window/cs regex '\b(class|interface|if|else|for|foreach|while|do|switch|case|return|public|private|protected|static|void|int|double|float|string)\b' 0:keyword
    add-highlighter window/cs regex '\b(Console|Math|List|Dictionary|HashSet)\b' 0:function
    add-highlighter window/cs regex '//.*$' 0:comment
}

hook global WinSetOption filetype=css %{
    add-highlighter window/css regex '\b(div|span|body|html|class|id|font|color|background|margin|padding|display|position)\b' 0:keyword
    add-highlighter window/css regex '\b(flex|grid|block|inline|relative|absolute|fixed)\b' 0:keyword
}

hook global WinSetOption filetype=html %{
    add-highlighter window/html regex '\b(html|head|body|div|span|p|a|img|table|tr|td|form|input|button|script|style)\b' 0:keyword
    add-highlighter window/html regex '\b(id|class|src|href|alt|type|value)\b' 0:attribute
}

hook global WinSetOption filetype=json %{
    add-highlighter window/json regex '\b(true|false|null)\b' 0:value
    add-highlighter window/json regex '\b([a-zA-Z][a-zA-Z0-9]*)\s:' 1:attribute
}

hook global WinSetOption filetype=julia %{
    add-highlighter window/julia regex '\b(function|if|else|elseif|for|while|break|continue|return|struct|module|using|import)\b' 0:keyword
    add-highlighter window/julia regex '\b(println|print|Array|Dict|Set|Float64|Int64)\b' 0:function
    add-highlighter window/julia regex '#.*$' 0:comment
}

hook global WinSetOption filetype=kotlin %{
    add-highlighter window/kotlin regex '\b(fun|class|interface|if|else|for|while|when|return|val|var|private|public|protected|override)\b' 0:keyword
    add-highlighter window/kotlin regex '\b(println|String|Int|Double|List|Map|Set)\b' 0:function
    add-highlighter window/kotlin regex '//.*$' 0:comment
}

hook global WinSetOption filetype=lua %{
    add-highlighter window/lua regex '\b(function|if|else|elseif|for|while|do|end|break|return|local|require)\b' 0:keyword
    add-highlighter window/lua regex '\b(print|table|string|math|io)\b' 0:function
    add-highlighter window/lua regex '--.*$' 0:comment
}

hook global WinSetOption filetype=markdown %{
    add-highlighter window/markdown regex '\b(#[# ].$|[+-]\s.$|\[.\]\(.\))\b' 0:keyword
    add-highlighter window/markdown regex '\b(_|\*\*||\*)\b' 0:keyword
}

hook global WinSetOption filetype=perl %{
    add-highlighter window/perl regex '\b(sub|if|else|elsif|for|foreach|while|do|return|use|my|our|local)\b' 0:keyword
    add-highlighter window/perl regex '\b(print|say|open|close|split|join)\b' 0:function
    add-highlighter window/perl regex '#.*$' 0:comment
}

hook global WinSetOption filetype=php %{
    add-highlighter window/php regex '\b(function|class|if|else|elseif|for|while|switch|case|break|return|public|private|protected)\b' 0:keyword
    add-highlighter window/php regex '\b(echo|print|array|string|int|float)\b' 0:function
    add-highlighter window/php regex '//.*$' 0:comment
    add-highlighter window/php regex '#.*$' 0:comment
}

hook global WinSetOption filetype=powershell %{
    add-highlighter window/powershell regex '\b(function|if|else|elseif|for|foreach|while|switch|break|continue|return|param)\b' 0:keyword
    add-highlighter window/powershell regex '\b(Write-Host|Get-Item|Set-Item|New-Item)\b' 0:function
    add-highlighter window/powershell regex '#.*$' 0:comment
}

hook global WinSetOption filetype=r %{
    add-highlighter window/r regex '\b(function|if|else|for|while|break|next|return|library|source)\b' 0:keyword
    add-highlighter window/r regex '\b(print|cat|data.frame|list|matrix|vector)\b' 0:function
    add-highlighter window/r regex '#.*$' 0:comment
}

hook global WinSetOption filetype=scala %{
    add-highlighter window/scala regex '\b(def|class|object|trait|if|else|for|while|return|val|var|case|match)\b' 0:keyword
    add-highlighter window/scala regex '\b(println|Array|List|Map|Set|Option)\b' 0:function
    add-highlighter window/scala regex '//.*$' 0:comment
}

hook global WinSetOption filetype=sql %{
    add-highlighter window/sql regex '\b(SELECT|FROM|WHERE|INSERT|UPDATE|DELETE|CREATE|TABLE|INDEX|JOIN|ON|GROUP|BY|ORDER|HAVING)\b' 0:keyword
    add-highlighter window/sql regex '\b(COUNT|SUM|AVG|MIN|MAX|DISTINCT)\b' 0:function
    add-highlighter window/sql regex '--.*$' 0:comment
}

hook global WinSetOption filetype=swift %{
    add-highlighter window/swift regex '\b(func|class|struct|enum|if|else|for|while|switch|case|break|continue|return|let|var)\b' 0:keyword
    add-highlighter window/swift regex '\b(print|String|Int|Double|Array|Dictionary)\b' 0:function
    add-highlighter window/swift regex '//.*$' 0:comment
}

hook global WinSetOption filetype=toml %{
    add-highlighter window/toml regex '\b(table|array|string|integer|float|boolean|datetime)\b' 0:keyword
    add-highlighter window/toml regex '\b(\[\[?[a-zA-Z][a-zA-Z0-9]*\]\]?)\b' 0:keyword
    add-highlighter window/toml regex '#.*$' 0:comment
}

hook global WinSetOption filetype=xml %{
    add-highlighter window/xml regex '\b(tag|element|attribute|xml|version|encoding)\b' 0:keyword
    add-highlighter window/xml regex '\b(<!\[CDATA\[.*?\]\]>)\b' 0:string
}

hook global WinSetOption filetype=yaml %{
    add-highlighter window/yaml regex '\b(true|false|null)\b' 0:value
    add-highlighter window/yaml regex '\b([a-zA-Z][a-zA-Z0-9]*)\s:' 1:attribute
    add-highlighter window/yaml regex '#.*$' 0:comment
}

hook global WinSetOption filetype=asm %{
    add-highlighter window/asm regex '\b(mov|add|sub|mul|div|jmp|je|jne|call|ret|push|pop|int)\b' 0:keyword
    add-highlighter window/asm regex '\b(eax|ebx|ecx|edx|esi|edi|esp|ebp)\b' 0:value
    add-highlighter window/asm regex ';.*$' 0:comment
}

hook global WinSetOption filetype=clojure %{
    add-highlighter window/clojure regex '\b(def|fn|if|cond|let|loop|when|do|ns|require)\b' 0:keyword
    add-highlighter window/clojure regex '\b(str|map|vector|list|set|println)\b' 0:function
    add-highlighter window/clojure regex ';.*$' 0:comment
}

hook global WinSetOption filetype=coffeescript %{
    add-highlighter window/coffeescript regex '\b(function|if|else|for|while|return|class)\b' 0:keyword
    add-highlighter window/coffeescript regex '\b(console|Array|Object|Math)\b' 0:function
    add-highlighter window/coffeescript regex '#.*$' 0:comment
}

hook global WinSetOption filetype=d %{
    add-highlighter window/d regex '\b(void|int|float|double|if|else|for|while|switch|case|return|struct|class|interface)\b' 0:keyword
    add-highlighter window/d regex '\b(writeln|write|array|string)\b' 0:function
    add-highlighter window/d regex '//.*$' 0:comment
}

hook global WinSetOption filetype=dart %{
    add-highlighter window/dart regex '\b(class|if|else|for|while|return|void|int|double|String|bool)\b' 0:keyword
    add-highlighter window/dart regex '\b(print|List|Map|Set)\b' 0:function
    add-highlighter window/dart regex '//.*$' 0:comment
}

hook global WinSetOption filetype=elixir %{
    add-highlighter window/elixir regex '\b(def|defmodule|if|else|for|while|case|cond|do|end)\b' 0:keyword
    add-highlighter window/elixir regex '\b(IO|Map|List|Set|Atom)\b' 0:function
    add-highlighter window/elixir regex '#.*$' 0:comment
}

hook global WinSetOption filetype=elm %{
    add-highlighter window/elm regex '\b(module|if|then|else|case|of|let|in|type|alias)\b' 0:keyword
    add-highlighter window/elm regex '\b(List|Dict|Maybe|Result)\b' 0:function
    add-highlighter window/elm regex '--.*$' 0:comment
}

hook global WinSetOption filetype=fortran %{
    add-highlighter window/fortran regex '\b(program|if|else|do|while|return|integer|real|double|subroutine|function)\b' 0:keyword
    add-highlighter window/fortran regex '\b(print|write|read)\b' 0:function
    add-highlighter window/fortran regex '(!.*$)' 0:comment
}

hook global WinSetOption filetype=groovy %{
    add-highlighter window/groovy regex '\b(def|class|if|else|for|while|switch|case|return|public|private|protected)\b' 0:keyword
    add-highlighter window/groovy regex '\b(println|List|Map|String)\b' 0:function
    add-highlighter window/groovy regex '//.*$' 0:comment
}

hook global WinSetOption filetype=haskell %{
    add-highlighter window/haskell regex '\b(data|type|if|then|else|case|of|let|in|module|where)\b' 0:keyword
    add-highlighter window/haskell regex '\b(putStrLn|print|map|list|Maybe|IO)\b' 0:function
    add-highlighter window/haskell regex '--.*$' 0:comment
}

hook global WinSetOption filetype=haxe %{
    add-highlighter window/haxe regex '\b(class|interface|if|else|for|while|return|public|private|static)\b' 0:keyword
    add-highlighter window/haxe regex '\b(trace|Array|Map|String)\b' 0:function
    add-highlighter window/haxe regex '//.*$' 0:comment
}

hook global WinSetOption filetype=lisp %{
    add-highlighter window/lisp regex '\b(define|if|cond|let|lambda|begin|set!|do)\b' 0:keyword
    add-highlighter window/lisp regex '\b(car|cdr|cons|list|map)\b' 0:function
    add-highlighter window/lisp regex ';.*$' 0:comment
}

hook global WinSetOption filetype=nim %{
    add-highlighter window/nim regex '\b(proc|func|if|else|for|while|return|var|let|const)\b' 0:keyword
    add-highlighter window/nim regex '\b(echo|seq|table|string|int)\b' 0:function
    add-highlighter window/nim regex '#.*$' 0:comment
}

hook global WinSetOption filetype=objc %{
    add-highlighter window/objc regex '\b(interface|implementation|if|else|for|while|return|int|float|id)\b' 0:keyword
    add-highlighter window/objc regex '\b(NSLog|NSArray|NSDictionary|NSString)\b' 0:function
    add-highlighter window/objc regex '//.*$' 0:comment
}

hook global WinSetOption filetype=ocaml %{
    add-highlighter window/ocaml regex '\b(let|rec|if|then|else|for|while|match|with|type|module)\b' 0:keyword
    add-highlighter window/ocaml regex '\b(printf|List|Array|Map)\b' 0:function
    add-highlighter window/ocaml regex '\(\*.*\*\)' 0:comment
}

hook global WinSetOption filetype=pascal %{
    add-highlighter window/pascal regex '\b(program|begin|end|if|else|for|while|case|of|var|const)\b' 0:keyword
    add-highlighter window/pascal regex '\b(writeln|write|readln|read)\b' 0:function
    add-highlighter window/pascal regex '(\{.*\})' 0:comment
}

hook global WinSetOption filetype=prolog %{
    add-highlighter window/prolog regex '\b(if|then|else|not|is|fail|true|false)\b' 0:keyword
    add-highlighter window/prolog regex '\b(write|writeln|atom|number)\b' 0:function
    add-highlighter window/prolog regex '%.*$' 0:comment
}

hook global WinSetOption filetype=racket %{
    add-highlighter window/racket regex '\b(define|if|cond|let|lambda|begin|set!|do)\b' 0:keyword
    add-highlighter window/racket regex '\b(display|list|map|string|number)\b' 0:function
    add-highlighter window/racket regex ';.*$' 0:comment
}

hook global WinSetOption filetype=scheme %{
    add-highlighter window/scheme regex '\b(define|if|cond|let|lambda|begin|set!|do)\b' 0:keyword
    add-highlighter window/scheme regex '\b(display|list|map|string|number)\b' 0:function
    add-highlighter window/scheme regex ';.*$' 0:comment
}

hook global WinSetOption filetype=zig %{
    add-highlighter window/zig regex '\b(fn|if|else|for|while|return|const|var|struct|enum)\b' 0:keyword
    add-highlighter window/zig regex '\b(std|print|ArrayList|string)\b' 0:function
    add-highlighter window/zig regex '//.*$' 0:comment
}

set-face global keyword rgb:4ec9ff
set-face global function rgb:00ffff
set-face global string rgb:00cccc
set-face global value rgb:00ffff
set-face global comment rgb:6699cc
set-face global attribute rgb:00b3ff
set-face global Default rgb:ccffff,default
set-face global PrimarySelection rgb:002244,rgb:99ddee+r
set-face global PrimaryCursor rgb:000000,rgb:00ffff+b
set-face global SecondarySelection rgb:002244,rgb:66aabb+r
set-face global SecondaryCursor rgb:000000,rgb:009999+b
set-face global MenuForeground rgb:002244,rgb:00ffff
set-face global MenuBackground rgb:ccffff,default
set-face global Information rgb:00ffff,default
set-face global StatusLine rgb:00ffff,default
set-face global LineNumbers rgb:6699cc,default
set-face global LineNumberCursor rgb:00ffff,default
set-face global MatchingChar rgb:ffaaaa,default+b
set-face global Whitespace rgb:003366,default

set-option global matching_pairs ( ) { } [ ] < >

hook global NormalIdle .* %{
    evaluate-commands %sh{ printf '\e[2 q\e[?25h' > /dev/tty }
}
hook global InsertIdle .* %{
    evaluate-commands %sh{ printf '\e[6 q\e[?25h' > /dev/tty }
}
hook global PromptIdle .* %{
    evaluate-commands %sh{ printf '\e[6 q\e[?25h' > /dev/tty }
}

hook global KakEnd .* %{
    echo "Kakoune ready bitch!!!!!! Alt+H=help, Alt+A=files, Alt+N=notes"
}
