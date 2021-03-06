import requests
import xml.etree.ElementTree as ET

class LyricLoader:
    def __init__(self, info):
        self.lyric = (' ' * 10) + 'lyric not found.'
        
        data = ("""<?xml version="1.0" encoding="UTF-8"?>
        <SOAP-ENV:Envelope
        xmlns:SOAP-ENV="http://www.w3.org/2003/05/soap-envelope"
        xmlns:SOAP-ENC="http://www.w3.org/2003/05/soap-encoding"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xmlns:xsd="http://www.w3.org/2001/XMLSchema"
        xmlns:ns2="ALSongWebServer/Service1Soap"
        xmlns:ns1="ALSongWebServer"
        xmlns:ns3="ALSongWebServer/Service1Soap12">
        <SOAP-ENV:Body><ns1:GetResembleLyric2>
        <ns1:stQuery>
        <ns1:strTitle>%s</ns1:strTitle>
        <ns1:strArtistName>%s</ns1:strArtistName>
        <ns1:nCurPage>0</ns1:nCurPage>
        </ns1:stQuery>
        </ns1:GetResembleLyric2>
        </SOAP-ENV:Body>
        </SOAP-ENV:Envelope>
        """ % (info[1], info[0])).encode('utf-8')
        url = 'http://lyrics.alsong.co.kr/alsongwebservice/service1.asmx'
        print(data)
        try:
            response = requests.post(url, data=data,
                headers={
                    'content-type': 'application/soap+xml',
                },
            )

            tree = ET.ElementTree(ET.fromstring(response.text))

            for node in tree.iter():
                if 'strLyric' in node.tag:
                    self.lyric = node.text
                    return

        except Exception as e:
            print(e)


