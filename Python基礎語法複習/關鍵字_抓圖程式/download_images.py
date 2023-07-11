from simple_image_download import simple_image_download as simp

response = simp.simple_image_download

keywords = ["vtuber stream background フリー素材"]

for kw in keywords:
    response().download(kw, 100)
