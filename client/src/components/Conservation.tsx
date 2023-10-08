import { AlertTriangleIcon } from "lucide-react";
import { Alert, AlertDescription, AlertTitle } from "./ui/alert";

const Conservation = () => {
  return (
    <>
      <Alert className="md:w-1/2">
        <AlertTriangleIcon className="w-6 h-6 mr-2 fill-yellow-500" />
        <AlertTitle>Conservation Advice!</AlertTitle>
        <AlertDescription>
          <ul className="">
            <li>yo mama</li>
            <li>yo mama</li>
            <li>yo mama</li>
            <li>yo mama</li>
          </ul>
        </AlertDescription>
      </Alert>
    </>
  );
};

export default Conservation;
