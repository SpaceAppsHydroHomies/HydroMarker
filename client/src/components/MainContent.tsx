import React from "react";
import { Table } from "./ui/table";

const MainContent = () => {
  return (
    <div>
      <h1 className="text-4xl font-bold text-center">Waterbody :3</h1>
      <ul className="flex flex-col ">
        <li className="flex flex-row">
          <a
            href="https://www.epa.gov/waterdata"
            target="_blank"
            rel="noreferrer"
            className="text-blue-500 hover:text-blue-700"
          >
            EPA Water Data
          </a>
        </li>
        <li className="flex flex-row">
          <a
            href="https://www.epa.gov/waterdata/water-quality-data-wqx"
            target="_blank"
            rel="noreferrer"
            className="text-blue-500 hover:text-blue-700"
          >
            Water Quality Data
          </a>
        </li>
        <li className="flex flex-row">
          <a
            href="https://www.epa.gov/waterdata/water-quality-data-wqx"
            target="_blank"
            rel="noreferrer"
            className="text-blue-500 hover:text-blue-700"
          >
            Water Quality Data
          </a>
        </li>
        <Table />
      </ul>
    </div>
  );
};

export default MainContent;
