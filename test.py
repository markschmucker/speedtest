import requests
import time


class NewEndpointDownloader():
    def __init__(self, updated_since_minutes=10):
        self.status_code = "none"
        self.updated_since_minutes = updated_since_minutes
        self.session = self.make_session()
        self.raw = ''

    def make_session(self):
        return requests.session()

    def download(self):
        url = "https://api.lendingclub.com/api/investor/v1/secondarymarket/listings?updatedSince=%d" % self.updated_since_minutes
        header = {'Authorization': '7KQKSktIg/gBtMIDl7znlQCujXg=', 'Accept': 'text/csv'}
        try:
            resp = self.session.get(url, headers=header)
            self.status_code = resp.status_code
            self.status_code
            self.raw = resp.content
        except Exception:
            print 'no connection'
            self.status_code = '?'
            self.raw = ''


if __name__ == "__main__":
    for lookback in (60, 1, 1, 1, 1, 1):
        t0 = time.time()
        dl = NewEndpointDownloader(lookback)
        t1 = time.time()
        dl.download()
        t2 = time.time()
        print 'lookback'
        print 'init took %d ms' % ((t1 - t0) * 1000.)
        print 'download took %d ms' % ((t2 - t1) * 1000.)
        print 'status code: ', dl.status_code
        print 'got chars: ', len(dl.raw)


