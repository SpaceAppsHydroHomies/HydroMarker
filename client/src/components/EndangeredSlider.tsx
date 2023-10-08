import { Card, CardContent, CardHeader, CardTitle } from "./ui/card";

const images = ["cat1.jpg", "cat2.jpg", "cat3.jpg", "cat4.jpg"];

const EndangeredSlider = () => {
  return (
    <Card>
      <CardHeader>
        <CardTitle>Endangered Species</CardTitle>
      </CardHeader>
      <CardContent>
        <div className="flex overflow-x-auto">
          {images.map((image) => (
            <img
              className="w-52 h-52 rounded-xl object-cover"
              src={`/${image}`}
              alt="cat"
            />
          ))}
        </div>
      </CardContent>
    </Card>
  );
};

export default EndangeredSlider;
