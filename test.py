import base64, requests, time


class Downloader():
    def __init__(self):
        self.status_code = "none"
        self.session =  requests.session()
        self.raw = ''
        self.rand_acct = 'N0tRS1NrdElnL2dCdE1JRGw3em5sUUN1alhnPQ=='

    def download(self, lookback):
        url = "https://api.lendingclub.com/api/investor/v1/secondarymarket/listings?updatedSince=%d" % lookback
        header = {'Authorization': base64.b64decode(self.rand_acct), 'Accept': 'text/csv'}
        try:
            resp = self.session.get(url, headers=header)
            self.status_code = resp.status_code
            self.status_code
            self.raw = resp.content
        except Exception:
            print('no connection')
            self.status_code = '?'
            self.raw = ''


if __name__ == "__main__":
    dl = Downloader()
    for lookback in (180, 60, 1, 1, 1, 1, 1):
        t0 = time.time()
        dl.download(lookback)
        t1 = time.time()
        print('lookback: %d min' % lookback)
        print('download took %d ms' % ((t1 - t0) * 1000.))
        print('status code: ', dl.status_code)
        print('got chars: ', len(dl.raw))


