# Created on Fri Nov 25 09:52:57 AM EST 2022
#!/usr/bin/env bash
Subject=""
To=""
echo """
Dear Davar

This is a late Thanksgiving greeting~! Wish you have had a restful short break before the end of the busy semester.

Nick (my Ph.D. student who graduated in the past summer) and I have been working on the revision carefully according to the referee report. I went to Brin Math Institute for a Workshop for SPDEs last week, invited by Yu Gu and Sandra. I had chance to talk to Yu about his work on the stationary limit. We figured out the differences between our work and his. In the revision, we have included Yu's paper and made some comments on that. More details can be found in the file -- Answers.pdf.

Indeed, I presented this work at the recent conference at Brin Math institute. The slides are attached for your convenience just in case it may interest you as well.

Regarding the paper, thank you very much for suggesting the alternatives, both Bernoulli and JTP. If you find the current version is acceptable, we will proceed to submit it to Bernoulli (first).

Thank you so much for your time and help!

Best regards,

Le
""" > tmp.txt
email-process tmp.txt
# neomutt -F ~/.config/mutt/muttrc_gmail \
neomutt \
  -s "${Subject}" \
  -b chenle02@gmail.com \
  -- $To \
  < tmp.txt

  # -a File_to_attach \
  # -c le.chen@emory.edu \
  # -e "source test.mutt" \

rm tmp.txt
