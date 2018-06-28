import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
import os
import shutil
import glob



curfilePath = os.path.abspath(__file__)
curDir = os.path.abspath(os.path.join(curfilePath, os.pardir))
tmpDir = os.path.abspath(os.path.join(curDir,'tmp/'))


# remove old crawling data
try:
    shutil.rmtree(tmpDir)
except:
    pass

print("Enter Search Keyword (product or brand name to search):"),
pruduct = input()

def banner():

    print("Press 1 for Amazon")
    print("Press 2 for Shopclues")
    print("Press 3 for olx")
    print("Press 4 for Ebay")
    print("Press 5 for new website")



# Get the search keyword from the user


# configure logging
configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})

# get the project settings
s=get_project_settings()

# Change the depth limit here
# s['DEPTH_LIMIT'] = 2
process = CrawlerProcess(s)




def main():
    choice = int(input(''))
    if choice == 1:
        process.crawl('amazon', product=pruduct)
        process.start()
    elif choice == 2:
        process.crawl('shopclues', product=pruduct)
        process.start()
    elif choice == 3:
        process.crawl('olx', product=pruduct)
        process.start()
    elif choice == 4:
        process.crawl('ebay', product=pruduct)
        process.start()
    elif choice == 5:

        process.crawl('spider', product=pruduct)
        process.start()
    else:
        print("Invalid Choice")
        main()


if __name__ == '__main__':
    banner()
    main()

# Add results to results.csv file after crawling is complete
interesting_files = glob.glob(tmpDir+'/*.csv')
header_saved = False
with open('results.csv','wb') as fout:
    for filename in interesting_files:
        if os.path.getsize(filename) > 0:
            with open(filename) as fin:
                header = next(fin) 
                if not header_saved:
                    fout.write(header)
                    header_saved = True
                for line in fin:
                    fout.write(line)


print('Crawling Completed')