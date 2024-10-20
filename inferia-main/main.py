from file_watcher import watch_directory


async def watch_files():
    watch_directory("../data/files",pdf_callback)

    return True


async def pdf_callback():
    return True
