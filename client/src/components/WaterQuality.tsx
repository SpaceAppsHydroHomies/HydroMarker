import {
    HoverCard,
    HoverCardContent,
    HoverCardTrigger,
} from "@/components/ui/hover-card";
import { RxInfoCircled } from "react-icons/rx";
import {
    Card,
    CardContent,
    CardHeader,
    CardTitle,
} from "@/components/ui/card";
import { Progress } from "./ui/progress";

type WaterQualityProps = {
    waterQualityScore: number; // Specify the type of the prop
};
const WaterQuality: React.FC<WaterQualityProps> = ({ waterQualityScore }) => {
    return (
        <div>
            <Card>
                <CardHeader>
                    <CardTitle className="flex justify-between">
                        QHEI: {waterQualityScore}
                        <HoverCard openDelay={100} closeDelay={200}>
                            <HoverCardTrigger>
                                <RxInfoCircled size={22} />
                            </HoverCardTrigger>
                            <HoverCardContent style={{ fontSize: 15 }}>
                                The Qualitative Habitat Evaluation Index (QHEI) is a scientific measure used by environmental researches and agencies
                                to evaluate and monitor the quality of aquatic and riparian habitats.
                            </HoverCardContent>
                        </HoverCard>
                    </CardTitle>
                </CardHeader>
                <CardContent>
                    <Progress value={waterQualityScore} />
                </CardContent>
            </Card>
        </div >
    );
};

export default WaterQuality;
