import React from "react";
import SearchBar from "./SearchBar";
import { ModeToggle } from "./mode-toggle";

const Header = () => {
  return (
    <div className="flex justify-end py-3">
      <SearchBar />
      <ModeToggle />
    </div>
  );
};

export default Header;
