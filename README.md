# :cloud: Historical Weather Analysis

## :pushpin: Overview
This project helps tracking **global** weather changes for specified cities *(listed at the end of the Overview section)*.  
The main tracked metrics include: 
- **Minimum Temperature** - calculated as the annual mean minimum temperature, then averaged across all years 
- **Maximum Temperature** - calculated as the annual mean maximum temperature, then averaged across all years 
- **Average Temperature** - calculated as the annual mean average temperature, then averaged across all years 
- **Precipitation Sum** - calculated as the annual precipitation sum, then averaged across all years 
- **Snow Sum** - calculated as the annual snow sum, then averaged across all years  
- **Sunshine Time Sum** *(only in **summary** view)* - calculated as the annual sunshine time sum, then averaged across all years   

[Link to the published report](https://app.powerbi.com/view?r=eyJrIjoiZWNiMWZjMTQtMTZkZS00ZWQyLTlkZTQtYTQ5NGQzNGExYmU3IiwidCI6ImZlYjM4NTE4LTFmMGUtNDVkOS1hNzA1LWUyMDZiZWQ5MWI1ZCIsImMiOjl9&pageName=4d87d0aa3588cde68060) *(at some moment it will not be accessible anymore)*  

Gif preview :point_down:  
![summary-page-demo.gif](Power%20BI/Screenshots/hwd_summary_page_demo.gif)
![detail-page-demo.gif](Power%20BI/Screenshots/hwd_detail_page_demo.gif)

The tracked cities are:
- Athens, Greece
- Berlin, Germany
- Helsinki, Finland
- Istanbul, Türkiye
- Kyiv, Ukraine
- London, UK
- Lviv, Ukraine
- Madrid, Spain
- Paris, France
- Stockholm, Sweden
- Vilnius, Lithuania

## :page_with_curl: Pages

1. :globe_with_meridians: **Summary** - compares key weather metrics between the cities.  
![summary.png](Power%20BI/Screenshots/hwd_summary.png)  
**Year** & **Season** filters are placed at the top right of the page. They leverage the interactivity of the displayed data and facilitate understanding weather trends within a specific date period or season.  
**Detail View** page navigation button is placed at the top left of the page. It jumps you the **Detail** page. 

2. :mag: **Detail** - highlights main trends & insights for a specific city.  
![detail.png](Power%20BI/Screenshots/hwd_detail.png)  
**Season** filter is placed at the top right of the page. It helps understanding weather trends within a specifc season.  
**Summary View** page navigation button is placed at the top left of the page. It jumps you the **Summary** page.    
**City** filter is placed on the right, vertically centered. It allows to switch between cities uncovering each city unique weather patterns.  
**Metric Switcher** is placed at the bottom right of the page. It empowers to change the displayed metric on a *Line Chart* and *Variation by Wind Direction* visuals. :point_down:  
![detail-metric-switcher.png](Power%20BI/Screenshots/hwd_detail_metric_switcher.png)  
### :question: Delta Numbers
As for the *delta* numbers - the ones that are displayed on the top five card visuals & between the values on the line chart - they show the growth of the corresponding metric between the current year bin *(last 5 years for card visuals)* and all the prior years.  
For example: for card visuals it is *2020-2024 vs 1950-2019*, for line chart at the point of 2010 it is *2010-2014 vs 1950-2009*.

## :sparkles: Insights
1. Summary
    - Winter
        - Kyiv, Helsinki, Vilnius have the **coldest** winters
        - Athens, Istanbul & Madrid have the **hottest** winters
        - London & Paris have pretty **mild** winters
        - Istanbul has a lot of **precipitation** in winter
        - Helsinki is the leader in **snow**
    - Summer
        - Athens, Istanbul & Madrid have the **hottest** summers but Kyiv is the fourth
        - Helsinki, London, Stockholm & Vilnius have **mild** summers
        - London has the least **sunshine** in summer
        - Athens, Madrid & Istanbul have little **rain** in summer
    - Overall
        - Vilnius has the least **sunshine**
        - ...I encourage you to get your own insights :alien:
2. Detail  
:hotsprings: Well, guys, global warming is real. Especially, it's actual for summer & winter. 

## :paperclip: Data Source
The report is built on the historical weather data provided by [Open-Meteo](https://open-meteo.com/en/docs/historical-weather-api).

## :file_folder: Project Structure
<pre>
/
├─ ETL/
│  ├─ alembic/
│  │  ├─ ...
│  ├─ db/
│  │  ├─ models/
│  │  │  ├─ __init__.py
│  │  │  ├─ base.py
│  │  │  ├─ location.py
│  │  │  ├─ weather_data.py
│  │  ├─ methods/
│  │  │  ├─ location.py
│  │  │  ├─ weather_data.py 
│  │  ├─ db_config.py
│  ├─ logger/
│  │  │  ├─ logger_setup.py 
│  ├─ .env (gitignore)
│  ├─ .gitignore
│  ├─ alembic_help.txt
│  ├─ alembic.ini
│  ├─ logs.txt (gitignore)
│  ├─ main.py
│  ├─ requirements.txt
├─ Power BI/
│  ├─ Assets/
│  │  ├─ ...
│  ├─ Screenshots/
│  │  ├─ ...
│  ├─ Historical Weather Data.pbix
├─ README.md
</pre>

## :hammer_and_wrench: Tools Used
- Power BI Desktop - be careful -> a lot of `DAX` used for measures, calculated columns & tables
- PostgreSQL - to store data
- Python - to extract & load data
    - `SQLAlchemy` - to harness ORM approach within database operations *(query and insert data)*
    - `alembic` - to create & run database migrations
    - `requests` - to extract data from [Open-Meteo](https://open-meteo.com/en/docs/historical-weather-api) source
    - `datetime`
    - `time`
    - `dotenv`
    - `logging`
- Figma - to build a custom background for report pages

## :electric_plug: Installation Instructions (Windows)
```bash
git clone https://github.com/volod-karpenko/Historical-Weather-Data-Project.git
cd Historical-Weather-Data-Project/ETL
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
These commands clone the repository, change the directory to the root folder of ```main.py```, initialize python virtual environment for the project, activate it & install the libraries.   
If you encounter errors while installing libraries, this command may help (be sure to run it within your venv):
```bash
pip install --upgrade pip setuptools
```
After you configure the ```.env``` file & set up the database ([you can download the backup here](https://drive.google.com/file/d/1-yQWrueaX9XanQz3wLWNb4JRix7ndQxD/view?usp=sharing)), go to ```Historical-Weather-Data-Project/ETL``` folder & run in cmd:
```bash
python main.py
```
```.env``` contains only one variable which is the database connection string  
```DATABASE_URL = postgresql+psycopg2://user:password@host/database```

## :pill: What Can Be Improved?
The potential problem is the amount of weather data imported into Power BI. For this moment, the grain of data loaded into Power BI is at the level of *individual location-individual date*. Thus, from 1950 to 2024 for eleven locations represented this loads around 300k of rows. Adding more locations will load more data and this could slow down interaction within the **Detail** page significantly. 
The potential solution is to aggregate the data by location, year and month decreasing the number of rows by ~30 times. Though, the complexity appears within wind directions - it's not that easy to aggregate them, though possible. To tell the truth, I've decided not to block myself with optimization while the number of locations is still & the perfomance is fast enough. 

## :raising_hand_man: Author
Volodymyr Karpenko  
[LinkedIn](https://www.linkedin.com/in/volod-karpenko/) • <a href=mailto:volod1701@gmail.com>Email </a>(volod1701@gmail.com)