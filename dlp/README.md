## Image Redaction
[DLP Doc](https://cloud.google.com/dlp/docs/concepts-image-redaction)

Two parts, inspections and redaction. The inspection call returns the type detected, the pixel coordinate of the lower left corner, and the dimensions of the box.

Redaction actually masks with opaque rectangles

Inspection takes a base-64 encoded image.  Streamed to DLP using the content.inspect() method. It runs OCR, then DLP scans the OCR output for the config you set. Returns coordinates as noted above. If nothing sentive detected, returns an empty HTTP 200 OK.

Redaction is similar to detection, except it returns the base64 image with redaction box instead of the coordinate JSON doc. Instead of content.inspect(), we run content.redact(). If nothing detected, it returns the image unchanged.

[Redaction Doc](https://cloud.google.com/dlp/docs/redacting-sensitive-data-images)


