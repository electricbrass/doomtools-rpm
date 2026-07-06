function __doomfetch {
  local -r IFS=$'\n'
  local -r cur="$2"
  local -r prev="$3"

  local -Ar drivers=(
    [idgames]=1
    [doomshack]=1
    [dogsoft]=1
    [tspgpk]=1
    [tspgeuro]=1
    [austral]=1
  )

  local -Ar exclusiveopts=(
    [--version]=1
    [--help]=1
    [-h]=1
  )

  local -Ar opts=(
    [--lockfile]=1
    [--target]=1
    [--update]=1
    [--nolock]=1
  )

  local exclusive_seen=false
  local driver_seen=false
  local opt_seen=false
  local filename_seen=false
  local -A used
  for word in "${COMP_WORDS[@]:1}"; do
    [[ $word == "$cur" ]] && break
    [[ -v exclusiveopts[$word] ]] && exclusive_seen=true && continue
    [[ -v drivers[$word] ]] && driver_seen=true && continue
    [[ -v opts[$word] ]] && opt_seen=true && used["$word"]=1 && continue
    filename_seen=true
  done

  if $exclusive_seen; then
    return
  fi

  if [[ $prev == "--target" ]]; then
    compgen -V COMPREPLY -d -- "$cur"
    return
  fi

  if [[ $prev == "--lockfile" ]]; then
    compopt -o plusdirs
    compgen -V COMPREPLY -f -X "!*.lock" -- "$cur"
    return
  fi

  local -a complist=()

  local opt
  for opt in "${!opts[@]}"; do
    if ! [[ -v used[$opt] ]]; then
      complist+=("$opt")
    fi
  done

  if ! $driver_seen && ! $opt_seen && ! $filename_seen; then
    complist+=("${!drivers[@]}" "${!exclusiveopts[@]}")
  fi

  compgen -V COMPREPLY -W "${complist[*]}" -- "$cur"
}

complete -o filenames -F __doomfetch doomfetch
