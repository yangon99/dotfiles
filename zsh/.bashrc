#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '

export LINGO_18_HOME="/home/yangon/.local/lingo18"

export PATH="/home/yangon/.local/lingo18:$PATH"
