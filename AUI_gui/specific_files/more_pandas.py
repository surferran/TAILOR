"""
https://medium.com/ibm-watson-data-lab/notebooks-for-spreadsheet-users-6481c79ad980
after action of:
    !pip install pixiedust
from console window.
after that write:
    pixiedust.optOut() 
to disable data collection.

tip:
    https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/ :
    write in console: '%lsmagic'

"""
import pixiedust

import re
def extractSector(postcode):
    m = re.findall(r"^[A-Z]+", str(postcode))
    if len(m):
      return m[0]
    else:
      return ''


if __name__=='__main__':
    url = 'https://raw.githubusercontent.com/glynnbird/sampledata/master/housesales.csv'
    homes = pixiedust.sampleData(url,forcePandas=True)
    print homes.info()
    
    expensive_homes_in_london = homes.loc[homes.price > 1000000].loc[homes.district == 'LONDON']
    print len(expensive_homes_in_london)
    print expensive_homes_in_london 
    
    #################################
    print extractSector('W1A1AA')
#    'W'
    print extractSector('WC17XU')
#    'WC'
    #################################
#    To create a new column (‘sector’)
    homes['sector'] = homes.postcode.apply(extractSector)
    
    homes_by_sector = homes.groupby("sector").aggregate({"price":"median"}).reset_index().sort_values("price", ascending=False).head(20)
    
    # good fot ipython notebook.. :
    display(homes_by_sector)
    
    #notebook kernel relates:
    store
    