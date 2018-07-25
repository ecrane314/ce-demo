Link to instructions, sample data already downlaoded from bucket
https://cloud.google.com/community/tutorials/data-science-extraction

# API Key
No need to download API key unless running outside of either GCE or SDK

# Install pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py [--user]

# virtualenv install + packages
pip install virtualenv [--user]
virtualenv env
source env/bin/activate
pip install pydub, gdebi, ffmpeg

#ffmpeg if necessary
python unzip script installed via wget
http://http.us.debian.org/debian/pool/main/f/ffmpeg/ffmpeg_3.2.10-1~deb9u1_amd64.deb

#Install Client Libraries [--user]
pip install --upgrade google-cloud-storage \
google-cloud-speech google-cloud-language

#Run the Speech to Text analysis in async mode for long files
$BUCKET=<set source bucket path>
gcloud ml speech recognize-long-running gs://${BUCKET}/audio/*.wav --language-code 'en-US'

#Run NLP (language) Alpha version for Entity Analysis 
gcloud alpha ml language analyze-entities \
--content-file=gs://${BUCKET}/callTranscript/transcript{i}.json >> \
entityAlpha.json

#Run NLP (language) for Entity Analysis
gcloud ml language analyze-entities --content-file=gs://${BUCKET}/callTranscript/transcript{i}.json  >> entity.json

nohup for i in gs://crane-1318/CallData/*.wav; do gcloud ml speech \
recognize-long-running "$i" --language-code=en-US --filter-profanity >> \
"${i%.*}transcribe.json"; done &

nohup gcloud alpha ml speech recognize-long-running gs://${BUCKET}/CallData/*.wav --language-code=en-US --filter-profanity > transcriptAlpha/transcript9.json &

gcloud alpha ml speech recognize-long-running $i --language-code=en-US --filter-profanity > transcriptAlpha/${i}.json