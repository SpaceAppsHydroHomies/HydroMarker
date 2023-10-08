import { Card, CardHeader, CardTitle, CardContent } from "./ui/card";

const messages = [
  "Report any illegal chemical dumpings to 1-800-424-8802",
  "Avoid removing plants and vegetation from the area",
  "Use natural fertilizers and pesticides when possible",
  "Take your trash with you when you leave the area",
  "Keep an eye and steer clear of the endangered species!",
  "Don't bring any non-native species into the natural waters",
  "Please use your best judgment in order to make decisions that protect the environment"
];

const getRandomMessages = (count) => {
  const shuffled = messages.sort(() => 0.5 - Math.random());
  return shuffled.slice(0, count);
};

const formatMessagesWithBulletPoints = (messages) => {
  return messages.map((message) => `• ${message}`).join("<br />");
};

const Conservation = () => {
  const uniqueRandomMessages = getRandomMessages(3);
  const formattedMessages = formatMessagesWithBulletPoints(uniqueRandomMessages);

  return (
    <Card>
      <CardHeader>
        <CardTitle>Environment Preservation</CardTitle>
      </CardHeader>
      <CardContent>
        <div dangerouslySetInnerHTML={{ __html: formattedMessages }} />
      </CardContent>
    </Card>
  );
};

export default function App() {
  return (
    <div>
      <Conservation />
    </div>
  );
}
