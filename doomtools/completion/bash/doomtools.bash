function __doomtools {
  local -r IFS=$' '
  if ((${#COMP_WORDS[@]} > 2)); then
    COMPREPLY=()
    return
  fi
  local -r cur="$2"

  compgen -V COMPREPLY -W "--help -h --docs --settings --website --where --env --java --gui" -- "$cur"
}

complete -F __doomtools doomtools
