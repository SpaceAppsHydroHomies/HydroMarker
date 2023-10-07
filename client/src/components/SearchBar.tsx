import React from "react";
import { Input } from "@/components/ui/input";

function SearchBar() {
  return (
    <div className="search-bar">
      <Input type="text" placeholder="Search" />
    </div>
  );
}

export default SearchBar;
