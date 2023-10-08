import {
  HoverCard,
  HoverCardContent,
  HoverCardTrigger,
} from "@/components/ui/hover-card";
import { RxInfoCircled } from "react-icons/rx";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Progress } from "./ui/progress";
import { useState } from "react";

const WaterQuality = () => {
  const waterQualityScore = 69;
  const [isHovered, setIsHovered] = useState(false);
  return (
    <div>
      <Card>
        <CardHeader>
          <CardTitle className="flex justify-between">
            <h2> Water Quality Score</h2>
            <HoverCard openDelay={100} closeDelay={200}>
              <HoverCardTrigger>
                <RxInfoCircled size={22} />
              </HoverCardTrigger>
              <HoverCardContent>bruh moment</HoverCardContent>
            </HoverCard>
          </CardTitle>
        </CardHeader>
        <CardContent>
          <Progress value={waterQualityScore} />
        </CardContent>
        <CardContent>
          water so good :) quality is at: {waterQualityScore}
        </CardContent>
      </Card>
    </div>
  );
};

export default WaterQuality;
