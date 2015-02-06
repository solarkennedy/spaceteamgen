#!/bin/bash

FILES="
AdjectivesBefore.txt
Nouns.txt
Verbs.txt
OnVerbs.txt
OffVerbs.txt
PrefixParts.txt
BasePartsBefore.txt
BaseParts.txt
MundaneActions.txt
InstructionPatterns.txt
GenericMedalAchievements.txt
"

for FILE in $FILES; do
  wget -c -O "$FILE" "http://www.sleepingbeastgames.com/spaceteam/TranslationTool/Strings/$FILE"
  sleep 2
done

