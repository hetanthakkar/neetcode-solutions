import requests
import os
from urllib.parse import urlparse

header = "https://emergingtalent.contentcontroller.com/ScormEngineInterface/defaultui/player/js/dispatch-server-min.js?cache=4e6e4eb' \
  -H 'accept: text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'priority: u=1, i' \
  -H 'referer: https://emergingtalent.contentcontroller.com/ScormEngineInterface/defaultui/player/modern.html?configuration=AccountId%7C6%21ContentVaultPath%7C%2Fvault%2Fdc33af78-5810-4688-a273-b3420952cd1d%21EngineTenantName%7Ce3dde401-3796-49f8-9a58-859cba2168f5%21InjectPathMediaFile%7Ctrue%21VersionRestart%7Ctrue&preventRightClick=true&cc=en_US&cache=21.1.33.498&playerConfUrl=j&package=ApiCourseId%7C0425920e-3a9b-4f1b-859b-70442c98786c%21VersionId%7C0&registration=ApiRegistrationId%7Ced618b7d-21c7-4566-a788-cb3974433ef2%21InstanceId%7C0&tracking=true&forceReview=false' \
  -H 'sec-ch-ua: "Brave";v="125", "Chromium";v="125", "Not.A/Brand";v="24"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-gpc: 1' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36' \
  -H 'x-requested-with: XMLHttpRequest"


# {"url of .vtt or .mp4 or .pdf ":"filename with no extentions"}
jobs = {
    "https://emergingtalent.contentcontroller.com/vault/c3b92e5a-1f5a-41c5-8ce8-d11d5fe7204d/r/courses/c1c11e4a-9cbd-4a9d-ab24-0d865132df01/0/ACDv2%20EN%20Video%20M08%20Sect01.mp4": "00 Introduction",
    "https://emergingtalent.contentcontroller.com/vault/c3b92e5a-1f5a-41c5-8ce8-d11d5fe7204d/courses/c1c11e4a-9cbd-4a9d-ab24-0d865132df01/0/1637613600435_en_ACDv2_Module08_Sect01-high.mp4-EN_US.vtt": "00 Introduction",
    "https://emergingtalent.contentcontroller.com/vault/7b5a7cc1-d4a0-4909-8a88-d030019825c8/r/courses/61c1bef5-bd71-451a-ac07-f585c67e515a/1/ACDv2%20EN%20SG%20M08.pdf": "Student guide",
}


buf = header.splitlines()

header_dict = {}  # formatting the header to a dict
for i in buf:
    i = i.split(" ", 1)
    i[0] = i[0].replace(":", "")
    i[0] = i[0].replace(" ", "")
    header_dict[i[0]] = i[1]

# print(header_dict["User-Agent"])

for url, filename in jobs.items():

    r = requests.get(url=url, headers=header_dict)

    a = urlparse(url)
    a = os.path.basename(a.path)

    asdf, file_extension = os.path.splitext(a)
    filename = filename.replace(":", "_")
    filename = filename.replace(" ", "_")
    filename = filename.replace("/", "_")

    filename = f"/path/to/your/folder/Module_08/{filename}{file_extension}"

    print(f"Downloaded {filename}")
    open(filename, "wb").write(r.content)
