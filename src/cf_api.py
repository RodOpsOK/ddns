import CloudFlare
from src.filters.records import RecordsFilter

class CFConnect:

    cf = None
    domain = None
    zoneID = None

    def __init__(self, domain, token):
        self.cf = CloudFlare.CloudFlare(token=token)
        self.domain = domain
        self.zoneID = self.getZoneInfo()['id']

    def getZoneInfo(self):
        return self.cf.zones.get(params={"name": self.domain})[0]

    def getRecords(self):
        return RecordsFilter(self.cf.zones.dns_records.get(self.zoneID, params={"per_page" : 5000}))

    def addRecord(self, dns_records):
        for record in dns_records:
            self.cf.zones.dns_records.post(self.zoneID, data=record)

    def updateRecord(self, record_id, data):
        return self.cf.zones.dns_records.patch(self.zoneID, record_id, data=data)

    def removeRecord(self, recordID):
        return self.cf.zones.dns_records.delete(self.zoneID, recordID)