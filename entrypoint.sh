#!/bin/sh

# Replace env vars in JavaScript files
echo "Replacing env vars in JS"
for file in /app/static/js/app.*.js;
do
  echo "Processing $file ...";

  # Use the existing JS file as template
  if [ ! -f $file.tmpl.js ]; then
    cp $file $file.tmpl.js
  fi

  envsubst '$VUE_APP_API_URL' < $file.tmpl.js > $file
done

uvicorn main:app --host 0.0.0.0 --port 80
