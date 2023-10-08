import Conservation from "./Conservation";
import EndangeredSlider from "./EndangeredSlider";
import WaterQuality from "./WaterQuality";
import { useState, useEffect } from "react";

const MainContent = (longlati: any) => {
  const [waterQualityData, setWaterQualityData] = useState<{}>({}); // Replace with your actual data
  useEffect(() => {
    (async () => {
      const [lat, lng] = [longlati.longlati.lat, longlati.longlati.lng];
      const apiUrl = `http://127.0.0.1:8000/water_quality/get_data/38.17248583506758/-98.21697191895801`;
      try {
        // Fetch data from the API using the fetch() function
        const data = await fetch(apiUrl)
          .then((response) => response.json())
          .then((responseData) => {
            console.log(responseData);
            // Set the state variable using the data returned from the API
            setWaterQualityData(responseData);
          });
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    })();
  }, []);
  return (
    <div className="flex flex-col gap-4">
      <h1 className="text-4xl font-bold">{waterQualityData.displayName}</h1>
      <WaterQuality waterQualityScore={waterQualityData.score} />
      <div className="flex flex-col md:flex-row gap-4">
        <EndangeredSlider waterQuality={waterQualityData} />
        <Conservation />
      </div>
    </div>
  );
};

export default MainContent;
