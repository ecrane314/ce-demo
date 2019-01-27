set +o history 2>/dev/null || setopt HIST_IGNORE_SPACE 2>/dev/null
 touch ~/.gitcookies
 chmod 0600 ~/.gitcookies

 git config --global http.cookiefile ~/.gitcookies

 tr , \\t <<\__END__ >>~/.gitcookies
source.developers.google.com,FALSE,/,TRUE,2147483647,o,git-ecrane314.gmail.com=1/fR6JHsigI-8S2GLgQi7RHztrXW6Cov9YScu_ish_Yzo
__END__
set -o history 2>/dev/null || unsetopt HIST_IGNORE_SPACE 2>/dev/null

