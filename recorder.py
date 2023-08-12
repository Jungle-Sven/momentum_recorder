import requests
import time
import pandas as pd
from datetime import datetime

class MomentumR:
    def get_data(self):
        your_ip = '123.456.789.000'
        url = f'http://{your_ip}:8083/api/momentum'
        try:
            r = requests.get(url)

            try:
                response = r.json()
                result = response['data']
            except Exception as e:
                result = None
                print(time.time(), e)                
            
        except Exception as e:
            #if api does not answer - create a blank event
            result = None
            print(time.time(), e)
            
        return result

    def create_df(self, data):
        lines = []
        timestamp = datetime.utcnow()
        for item in data:
            lines.append([timestamp, item['symbol'], item['timestamp'], item['price'], \
                      item['momentum_signal'], item['signal_with_direction'], \
                    item['change_signal']])
        df= pd.DataFrame(lines, columns=['recieve_timestamp', 'symbol', \
                                         'timestamp', 'price', 'momentum_signal', \
                                        'signal_with_direction', 'change_signal'])
        return df

    def save_data(self, df):
        filename = '/usr/storage/dataset.csv'
        df.to_csv(filename, mode='a', header=False, index=False)

    def run(self):
        while True:
            try:
                time.sleep(1)
                data = self.get_data()
                if data:
                    df = self.create_df(data)
                    self.save_data(df)
            except Exception as e:
                print(f'MomentumR error: {e}')
            
if __name__ == '__main__':
    test = MomentumR()
    test.run()


    