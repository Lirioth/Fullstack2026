// Daily Challenge — Creating Objects (TypeScript, Single File)
// ------------------------------------------------------------
// Implements a Video class with constructor params: title, uploader, time (seconds).
// Includes a .watch() method and demos (guarded). Exports provided for reuse/testing.

export class Video {
  public title: string;
  public uploader: string;
  public time: number; // seconds

  constructor(title: string, uploader: string, time: number) {
    this.title = title;
    this.uploader = uploader;
    this.time = time;
  }

  // Displays: "uploader watched all time seconds of title!"
  public watch(): string {
    return `${this.uploader} watched all ${this.time} seconds of ${this.title}!`;
  }
}

// Instantiate two examples
export const video1 = new Video("Intro to TypeScript", "Kevin", 420);
export const video2 = new Video("Advanced Array Methods", "Lirioth", 900);

// Bonus: preferred data structure → array of objects with named fields for clarity.
export type VideoData = { title: string; uploader: string; time: number };

export const videosData: VideoData[] = [
  { title: "JS Basics", uploader: "Ada", time: 300 },
  { title: "DOM Manipulation", uploader: "Grace", time: 480 },
  { title: "Async Patterns", uploader: "Linus", time: 660 },
  { title: "Functional JS", uploader: "Tim", time: 540 },
  { title: "Testing 101", uploader: "Alex", time: 360 },
];

// Instantiate from the array
export const videos: Video[] = videosData.map(v => new Video(v.title, v.uploader, v.time));

// ------------------------
// Optional demo (guarded):
// ------------------------
declare const require: any | undefined;
declare const module: any | undefined;

if (typeof require !== "undefined" && typeof module !== "undefined" && require.main === module) {
  console.log(video1.watch());
  console.log(video2.watch());
  videos.forEach(v => console.log(v.watch()));
}
