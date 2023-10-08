import Conservation from "./Conservation";
import EndangeredSlider from "./EndangeredSlider";
import WaterQuality from "./WaterQuality";

const MainContent = () => {
  return (
    <div className="flex flex-col gap-2">
      <h1 className="text-4xl font-bold">Waterbody :3</h1>

      <WaterQuality />
      <div className="flex flex-col md:flex-row gap-2">
        <EndangeredSlider />
        <Conservation />
      </div>
    </div>
  );
};

export default MainContent;
