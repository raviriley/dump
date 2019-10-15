#!/bin/bash
#
# matrix: matrix-ish display for Bash terminal
# Author: Brett Terpstra 2012 <http://brettterpstra.com>
# Contributors: Lauri Ranta and Carl <http://blog.carlsensei.com/>
#
# A morning project. Could have been better, but I'm learning when to stop.

### Customization:
blue="\033[0;34m"
brightblue="\033[1;34m"
cyan="\033[0;36m"
brightcyan="\033[1;36m"
green="\033[0;32m"
brightgreen="\033[1;32m"
red="\033[0;31m"
brightred="\033[1;31m"
white="\033[1;37m"
black="\033[0;30m"
grey="\033[0;37m"
darkgrey="\033[1;30m"
purple="\033[0;35m"
brightpurple="\033[1;37m"
brown="\033[0;33m"
yellow="\033[1;33m"
all=($blue $brightblue $cyan $brightcyan $green $brightgreen $red $brightred $white $black $grey $darkgrey $purple $brightpurple $brown $yellow)
google=($blue $red $yellow $green)

# Choose the colors that will be used from the above list
# space-separated list
# e.g. `colors=($green $brightgreen $darkgrey $white)`
colors=("${all[@]}") #all colors
#colors=("${google[@]}") #google colors
#colors=($green $brightgreen) # hollywood
#colors=($purple $brightpurple $green $brightgreen) #whatever you want
### End customization

### Do not edit below this line
spacing=${1:-100} # the likelihood of a character being left in place
scroll=${2:-0} # 0 for static, positive integer determines scroll speed
screenlines=$(expr `tput lines` - 1 + $scroll)
screencols=$(expr `tput cols` / 2 - 1)

chars=(a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 0 1 2 3 4 5 6 7 8 9 ^)
#chars=(neato neat Neat Neato)

count=${#chars[@]}
if [ $colors == $all ]
then
	colorcount=${#all[@]}
else
	colorcount=${#colors[@]}
fi


trap "tput sgr0; clear; exit" SIGTERM SIGINT

if [[ $1 =~ '-h' ]]; then
	echo "Display a Matrix(ish) screen in the terminal"
	echo "Usage:		matrix [SPACING [SCROLL]]"
	echo "Example:	matrix 100 0"
	exit 0
fi


clear
tput cup 0 0
while : 
do for i in $(eval echo {1..$screenlines})
	do for i in $(eval echo {1..$screencols})
		do rand=$(($RANDOM%$spacing))
			case $rand in
				0)
					printf "${colors[$RANDOM%$colorcount]}${chars[$RANDOM%$count]} "
					;;
				1)
					printf "  "
					;;
				*)
					printf "\033[2C"
					;;
			esac
		done
		printf "\n"

		# sleep .005
	done
	tput cup 0 0
done
