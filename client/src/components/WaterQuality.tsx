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

const WaterQuality = () => {
  const waterQualityScore = 69;
  return (
    <div>
      <Card>
        <CardHeader>
          <CardTitle className="flex justify-between">
            WQI: {waterQualityScore}
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
      </Card>
    </div>
  );
};

export default WaterQuality;
