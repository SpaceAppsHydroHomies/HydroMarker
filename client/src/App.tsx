import { Helmet } from "react-helmet";
import { motion } from "framer-motion";

import Header from "./components/Header";
import MainContent from "./components/MainContent";
import Map from "./components/Map";

function App() {
  return (
    <>
      <Helmet>
        <title>WaterTime :3</title>
        <link rel="icon" href="/favicon_io/favicon.ico" />
        <link rel="apple-touch-icon" href="/favicon_io/apple-touch-icon.png" />
        <link rel="manifest" href="/favicon_io/site.webmanifest" />
      </Helmet>
      <div className="container">
        <Header />
        <MainContent />
      </div>
      <motion.div
        className="w-64 h-64 absolute bottom-5 right-5"
        // drag // Enables dragging
        // dragConstraints={{ left: 1, right: 1, top: 1, bottom: 1 }} // Optional: Constraints for dragging
      >
        <motion.div className="w-full h-full p-2 pt-8 bg-slate-600 rounded-xl ">
          <Map />
        </motion.div>
      </motion.div>
    </>
  );
}

export default App;
