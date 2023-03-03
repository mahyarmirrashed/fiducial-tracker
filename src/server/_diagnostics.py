from src.common import display


def show_status(args, *, running: bool) -> None:
  if running:
    state = f"\x1b[42;1mServer is [RUNNING]\x1b[0m"
  else:
    state = f"\x1b[41;1mServer is [STOPPED]\x1b[0m"

  display(
    f"""{state}
  Video stream address:     {args.video_stream_address}
  Location stream address:  {args.location_stream_address}
  Publish frequency:        {args.frequency:.2} Hz
  
  Display raw frames:       {"Yes" if args.display_raw_frames else "No"}
  Display processed frames: {"Yes" if args.display_processed_frames else "No"}
  Save raw frames:          {"Yes" if args.save_raw_frames else "No"}
  Save processed frames:    {"Yes" if args.save_processed_frames else "No"}"""
  )
