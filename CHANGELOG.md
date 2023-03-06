

## [0.14.2](https://github.com/mahyarmirrashed/fiducial-tracker/compare/0.14.1...0.14.2) (2023-03-06)

## [0.14.1](https://github.com/mahyarmirrashed/fiducial-tracker/compare/0.14.0...0.14.1) (2023-03-04)


### Bug Fixes

* enable negative values for view for proper transformations ([cb1a024](https://github.com/mahyarmirrashed/fiducial-tracker/commit/cb1a0247b2d629061733e037ca38cd3a92ba0576))
* properly extract height and width parameters from frame shape ([f5f7279](https://github.com/mahyarmirrashed/fiducial-tracker/commit/f5f7279ee0b8b3d8f39535d5facf232467128c09))
* **server:** calibrate heading to orientation of view rectangle ([1a7b5d9](https://github.com/mahyarmirrashed/fiducial-tracker/commit/1a7b5d9e924db964d6b9870e35b3c536c27d1e6c))

## [0.14.0](https://github.com/mahyarmirrashed/fiducial-tracker/compare/0.13.0...0.14.0) (2023-03-04)


### Features

* **camera:** add ability to enable color stream if needed ([dca4a19](https://github.com/mahyarmirrashed/fiducial-tracker/commit/dca4a195240429430e482b2dd31c2f74ecfd1fa4))
* **server:** add heading information for tracked fiducials ([6b87ce3](https://github.com/mahyarmirrashed/fiducial-tracker/commit/6b87ce3ebbf8b2233655c97a43912aa8aa86cdd6))
* **server:** use `zxing-cpp` instead of `pyzbar` ([6216f35](https://github.com/mahyarmirrashed/fiducial-tracker/commit/6216f35d6cb08e4e16f6443c0f21771f2da50331))
* **server:** window manager to create separate windows for each input stream ([c5660e9](https://github.com/mahyarmirrashed/fiducial-tracker/commit/c5660e93b2d421a7457ac26035d944338e2599e8))
* **video_stream:** skip encoding step and send array as raw bytes along with shape information ([c26f118](https://github.com/mahyarmirrashed/fiducial-tracker/commit/c26f1188275d198fa3b0ec2ac1f3f8d2bf42a13d))


### Bug Fixes

* **camera:** allow `mkv` video file types ([7fcd64d](https://github.com/mahyarmirrashed/fiducial-tracker/commit/7fcd64dc44b234152034811dfd589df88b8c736b))
* prevent zero division possibility ([3523359](https://github.com/mahyarmirrashed/fiducial-tracker/commit/3523359108a14981053598cd54ef43c5cf0b1151))
* update open windows after pruning ([4ebb392](https://github.com/mahyarmirrashed/fiducial-tracker/commit/4ebb392e4bc8a4e033722cb7b8c685050fbec967))


### Performance Improvements

* **server:** add specification to only scan for QR codes ([9f683d4](https://github.com/mahyarmirrashed/fiducial-tracker/commit/9f683d4c829c59ed4e2cef9e4ec983c9843c34d4))

## [0.13.0](https://github.com/mahyarmirrashed/fiducial-tracker/compare/0.12.0...0.13.0) (2023-03-04)


### Features

* add ability to convert fiducial readily to dictionary ([699b255](https://github.com/mahyarmirrashed/fiducial-tracker/commit/699b2551e0f5865391aa27d0a87104a62910a538))
* add logger factory ([781ab3b](https://github.com/mahyarmirrashed/fiducial-tracker/commit/781ab3b132f310cf4a35aee7c8357f3b4d815795))
* add socket address model ([ff77488](https://github.com/mahyarmirrashed/fiducial-tracker/commit/ff7748826706dedc1a3891c57195669097be29a4))
* add socket address type for argument parsing ([4ebdb1c](https://github.com/mahyarmirrashed/fiducial-tracker/commit/4ebdb1c60fe18171d0d59b29a4185cc820d6b2ab))
* **camera:** add debugging message when server response times out ([55b5879](https://github.com/mahyarmirrashed/fiducial-tracker/commit/55b58797fe5e6560c8469d2df06bc519080ac189))
* **camera:** add logger object ([025af3e](https://github.com/mahyarmirrashed/fiducial-tracker/commit/025af3e5467d8d64bc8707cb60443588ea45fa89))
* **camera:** use camera logger for printing messages ([4059ff9](https://github.com/mahyarmirrashed/fiducial-tracker/commit/4059ff98999031ce631c7b4b8dee20d18b23c931))
* **camera:** use socket address rather than port number ([080ec93](https://github.com/mahyarmirrashed/fiducial-tracker/commit/080ec939bfc741feb7f53b4f087bc387f9ad6b00))
* **client:** add argument for supplying firebase rtdb certificate file ([a19bf84](https://github.com/mahyarmirrashed/fiducial-tracker/commit/a19bf844d4a08ff2b79f59ca316ee712b87ec1f0))
* **client:** add firebase connection provider ([09b5ca9](https://github.com/mahyarmirrashed/fiducial-tracker/commit/09b5ca9a42560d783ab6c897a113353e926dbf66))
* **client:** add logger object ([4d0ef34](https://github.com/mahyarmirrashed/fiducial-tracker/commit/4d0ef3484fae1103e4c145ef6d912eb8246b24ce))
* **client:** use client logger for printing messages ([32191d0](https://github.com/mahyarmirrashed/fiducial-tracker/commit/32191d0c614567905e7388472d71774950af1b92))
* convert all hostnames to ip addresses after initialization ([dc5e3e1](https://github.com/mahyarmirrashed/fiducial-tracker/commit/dc5e3e1fd41d9123ac49c403dbc538ae599fb62e))
* parse video stream address as full socket address ([95d655b](https://github.com/mahyarmirrashed/fiducial-tracker/commit/95d655beb9d2ea375c14483acdeba7e8f6bcaf50))
* **server:** add basic logging for start up and exit ([09a5117](https://github.com/mahyarmirrashed/fiducial-tracker/commit/09a51176abcf5744411752a955247651b8774fbc))
* **server:** add flag for showing server status rather than logging messages ([ab9c14a](https://github.com/mahyarmirrashed/fiducial-tracker/commit/ab9c14afa5dae2ad4f8476203a13f8db600e04eb))
* **server:** add logger object ([4106bf0](https://github.com/mahyarmirrashed/fiducial-tracker/commit/4106bf0c9f29f0a11c84cbbbaedd3fbabc8f6a0a))
* **server:** do not show status when flag is not set ([704b312](https://github.com/mahyarmirrashed/fiducial-tracker/commit/704b3120b1923783a2f9efc3d9496916cb7a6102))
* **server:** use socket address rather than port numbers ([4adecd1](https://github.com/mahyarmirrashed/fiducial-tracker/commit/4adecd1d8e9237afd15625af2f8c1508a85a46c5))


### Bug Fixes

* add logger factory as a module export ([3e01e1c](https://github.com/mahyarmirrashed/fiducial-tracker/commit/3e01e1c2eb8c12e646de0c4f6e5e925b0552169c))
* **camera:** immediately discard any unsent messages ([549cd4c](https://github.com/mahyarmirrashed/fiducial-tracker/commit/549cd4c5b888e419aa97b6c867bc8ce6ac64d7cd))
* custom `repr` for shortening decimal places ([9bf032f](https://github.com/mahyarmirrashed/fiducial-tracker/commit/9bf032f85b28c41b33b93bbb4dfbe448f9126b09))
* properly parse list fields ([5174905](https://github.com/mahyarmirrashed/fiducial-tracker/commit/51749059350df46302441015d3bd994da28eac58))
* set namespace variable for video stream address ([e8b27f9](https://github.com/mahyarmirrashed/fiducial-tracker/commit/e8b27f9557919d6af85bbeccbe5b7390aef2198c))

## [0.12.0](https://github.com/mahyarmirrashed/fiducial-tracker/compare/0.11.0...0.12.0) (2023-02-22)


### Features

* add ability to reset heartbeat ([093c8c9](https://github.com/mahyarmirrashed/fiducial-tracker/commit/093c8c92baaeb5342718a98c756c48e4f0595697))
* **camera:** create camera dataclass for better ui ([0a788e9](https://github.com/mahyarmirrashed/fiducial-tracker/commit/0a788e9e0a0bb1d1e22b145ed8035e0c88801af5))
* make point based on tuple of two floats ([ed90f85](https://github.com/mahyarmirrashed/fiducial-tracker/commit/ed90f85e5d8ff27514f4cedc90074fea2012d5ff))
* **models:** add dictionary mixin for serialization to python dictionaries ([4551956](https://github.com/mahyarmirrashed/fiducial-tracker/commit/4551956ad8a456f72d86ed0597e0c4650372d2e7))
* **server:** add heartbeat for regularly sending list of tracked fiducials to clients ([98f9cf9](https://github.com/mahyarmirrashed/fiducial-tracker/commit/98f9cf9c6a1266b647e685f4575a03e162073cef))
* **server:** properly scale and translate coordinate to world coordinates ([66ed6c4](https://github.com/mahyarmirrashed/fiducial-tracker/commit/66ed6c46d5201f08510fd0d2ed15fd3588bb537c))


### Bug Fixes

* **camera:** change coordinate system to match `opencv` ([b5eba7d](https://github.com/mahyarmirrashed/fiducial-tracker/commit/b5eba7d50607734411bd32cd1d1905775b23a80a))
* **camera:** cleanly exit on `KeyboardInterrupt` ([c18dc1a](https://github.com/mahyarmirrashed/fiducial-tracker/commit/c18dc1ab30017a7160eb584706167700a880c16a))
* **camera:** do not require direct show backend on linux ([f3b66da](https://github.com/mahyarmirrashed/fiducial-tracker/commit/f3b66dafba1cf844fec35d5ffad811dff407aefa))
* **camera:** keep consistent spacing on prompt options ([e96904f](https://github.com/mahyarmirrashed/fiducial-tracker/commit/e96904ff4d31e69d2e47cdd843bdf16ddcdb6720))
* **camera:** use proper `VideoReader` argument ([1cdca21](https://github.com/mahyarmirrashed/fiducial-tracker/commit/1cdca21debc1a61b61c189bfe90563f22b1ae7e1))
* specifically only handle `ValueError` ([b362f0a](https://github.com/mahyarmirrashed/fiducial-tracker/commit/b362f0a59f74c3e59ede8f48db8a09288ed296cd))
* use dictionary mixin methods ([50484e6](https://github.com/mahyarmirrashed/fiducial-tracker/commit/50484e697e2c2882253aac89a65e91698517aebf))

## [0.11.0](https://github.com/mahyarmirrashed/fiducial-tracker/compare/0.10.0...0.11.0) (2023-02-21)


### Features

* add `pyzbar` for qr code fiducial detection ([4fef12c](https://github.com/mahyarmirrashed/fiducial-tracker/commit/4fef12c45eb40402569571de2d4535c63d85555d))
* add ability to save raw frames ([1918ba5](https://github.com/mahyarmirrashed/fiducial-tracker/commit/1918ba5e803b49cc5a350258e5a3c246c684e747))
* add ability to view processed frames ([12a3083](https://github.com/mahyarmirrashed/fiducial-tracker/commit/12a3083b036cb0861f73bd0729db8776ca7395ee))
* add condition for showing raw frames ([20b12e9](https://github.com/mahyarmirrashed/fiducial-tracker/commit/20b12e9463e8a123b140bbe3e22319c2c652215c))


### Bug Fixes

* **camera:** enable direct show opencv backend ([c7d9d63](https://github.com/mahyarmirrashed/fiducial-tracker/commit/c7d9d6349076baa13723a56e0d7ab46947ff8e8e))
* disable ability to break using `q` key ([91b651b](https://github.com/mahyarmirrashed/fiducial-tracker/commit/91b651bd2d107490c23de1a4c9699b378bde3016))
* only time between receiving message and fully processing it ([6271c81](https://github.com/mahyarmirrashed/fiducial-tracker/commit/6271c815059d54ee14f606426c229b7a2c76895f))

## [0.10.0](https://github.com/mahyarmirrashed/fiducial-tracker/compare/0.9.0...0.10.0) (2023-02-17)


### Features

* add ability to load network from files ([eb6e037](https://github.com/mahyarmirrashed/fiducial-tracker/commit/eb6e037b75055ca8e24e143a1be24798816e2fd6))
* add bindings to shared library methods ([1f15523](https://github.com/mahyarmirrashed/fiducial-tracker/commit/1f155238c5590818e91fa835b85eb907adca0d78))
* add bounding box structure ([70878e6](https://github.com/mahyarmirrashed/fiducial-tracker/commit/70878e6654032ffa97641f3cc8ab98973159ff5a))
* add detection and count pair structure ([bd791b6](https://github.com/mahyarmirrashed/fiducial-tracker/commit/bd791b6a5118154029afc4b2af80c63ae986a9aa))
* add float range class ([e3975e2](https://github.com/mahyarmirrashed/fiducial-tracker/commit/e3975e23306aba1cedfe84b779dab7af6c0a8ca8))
* add image structure ([c8c0af7](https://github.com/mahyarmirrashed/fiducial-tracker/commit/c8c0af75353d5443de31c43db8c720e223d51a3f))
* add methods for accessing network height and width ([0d23fc2](https://github.com/mahyarmirrashed/fiducial-tracker/commit/0d23fc2da520078069e788342e5201c6ed5f0012))
* add network class for encapsulating resource and metadata ([128f355](https://github.com/mahyarmirrashed/fiducial-tracker/commit/128f355830e770535d143151af56d6c3a3a29277))
* add network classes metadata structure ([5d49c3d](https://github.com/mahyarmirrashed/fiducial-tracker/commit/5d49c3d400af82a2ca5dd824bfa00dfbc28e7c8e))
* add object detection structure ([9750013](https://github.com/mahyarmirrashed/fiducial-tracker/commit/97500135109c645dffc24f2742df5e556d775912))
* add parameter for setting number of decimal places ([41f9a92](https://github.com/mahyarmirrashed/fiducial-tracker/commit/41f9a92664ef757adbb9c1442e315aaeb376d5ce))
* add timing out on `recv` calls ([b75b91d](https://github.com/mahyarmirrashed/fiducial-tracker/commit/b75b91d1db6de1d97401e6159aadd23b9d4f30cb))
* allow passing file type as single string parameter ([6c6f7ed](https://github.com/mahyarmirrashed/fiducial-tracker/commit/6c6f7ed3456732342d108f48fac73863ce5b2de0))
* convert to `darknet` module ([1257604](https://github.com/mahyarmirrashed/fiducial-tracker/commit/1257604acdab92a9efb19952958e3dbfa1f09ad5))
* create library class for interfacing with `darknet` library ([27c8d7c](https://github.com/mahyarmirrashed/fiducial-tracker/commit/27c8d7c1497ff1d4bf0deafaa83b5a856c52326e))
* **darknet:** add ability to get predictions from the model on an image ([0632412](https://github.com/mahyarmirrashed/fiducial-tracker/commit/06324128a6fbe7425cbaba22ae28466057dd6f79))
* **darknet:** add normalizing and scaling abilities for bounding boxes ([03f454f](https://github.com/mahyarmirrashed/fiducial-tracker/commit/03f454fe82df66440003b14a6587cb931d681061))
* **models:** add helper methods for calculating view width and height from corners ([8ca728d](https://github.com/mahyarmirrashed/fiducial-tracker/commit/8ca728d06bfc8bb8cd8ca0d6738bd8bdf40757fb))
* only make instance of darknet library public ([78e0336](https://github.com/mahyarmirrashed/fiducial-tracker/commit/78e03362df77c92acf30e4b85e31ab0fe3d824fb))
* round float range type to specified number of decimal places ([5d543d3](https://github.com/mahyarmirrashed/fiducial-tracker/commit/5d543d376cdeb84fd021265a7eaa7a47486660ef))
* **server:** add ability to create image detection buffer ([09aeb93](https://github.com/mahyarmirrashed/fiducial-tracker/commit/09aeb935a39a218077eee2ccbb273e33a8e30b4d))
* **server:** add ability to set darknet threshold confidence ([866b03b](https://github.com/mahyarmirrashed/fiducial-tracker/commit/866b03b34642d7fb3c080336abf9a506139dbea2))
* **server:** add arguments for displaying and saving raw/processed frames ([bef3cfb](https://github.com/mahyarmirrashed/fiducial-tracker/commit/bef3cfb4f930e8f75aacac772b5572ac4de3a784))
* **server:** add configuration file argument ([966c98e](https://github.com/mahyarmirrashed/fiducial-tracker/commit/966c98e5e431f48a82690b9a158a825e33007bef))
* **server:** add data file argument ([f8c8594](https://github.com/mahyarmirrashed/fiducial-tracker/commit/f8c8594bca9ad4f84ef204ff9c042505e23bb2c5))
* **server:** add single-threaded inferencing using `darknet` interface ([f09035e](https://github.com/mahyarmirrashed/fiducial-tracker/commit/f09035eabc3ae34e26f1c4137181990bbe457f9e))
* **server:** add weights argument ([11dc5b3](https://github.com/mahyarmirrashed/fiducial-tracker/commit/11dc5b389856b8db23f404cfec4df2a5c2e109f3))
* **server:** allow recommended fps to be a float ([f5a0f85](https://github.com/mahyarmirrashed/fiducial-tracker/commit/f5a0f85bbb2e68de9ca6de761cfcea4fa0bb8cdd))


### Bug Fixes

* enable passing integers as arguments ([6083e9d](https://github.com/mahyarmirrashed/fiducial-tracker/commit/6083e9d92d8a9cae7eee2056b8e96b7664938c90))
* make bounding box dataclass frozen ([dafe515](https://github.com/mahyarmirrashed/fiducial-tracker/commit/dafe51534615c3aed2944715fc4c7371b9798b72))
* make float range type visible to other modules ([3e54408](https://github.com/mahyarmirrashed/fiducial-tracker/commit/3e54408201770ece5e4f32a670b3a98310120c76))
* should raise `TypeError` instead of `ValueError` ([eefd584](https://github.com/mahyarmirrashed/fiducial-tracker/commit/eefd5844cb49f94a35486252a9bb47c95b46cb6d))
* use strings as identifiers ([0c98aaa](https://github.com/mahyarmirrashed/fiducial-tracker/commit/0c98aaa991ee9e9be59fc171676e7c2aff1653fe))


### Reverts

* remove conversion of bounding box values to cv2 rectangle corners ([1b5912c](https://github.com/mahyarmirrashed/fiducial-tracker/commit/1b5912c64c19b4087dca728f184542eca094cdd6))
* use original index-based method until can test properly ([ba7fd9e](https://github.com/mahyarmirrashed/fiducial-tracker/commit/ba7fd9e128d2728e7c0d0711dd513cef4ab4b0c4))

## [0.9.0](https://github.com/mahyarmirrashed/fiducial-tracker/compare/0.8.0...0.9.0) (2023-02-07)


### Features

* add `recv` method for `VideoStreamResponseMessage` ([6e83983](https://github.com/mahyarmirrashed/fiducial-tracker/commit/6e8398308580f7e406d4e883fd03cb62caa85380))
* add camera fps regulator ([1eac9cb](https://github.com/mahyarmirrashed/fiducial-tracker/commit/1eac9cbc5b1064b11611f9ec7383f1bdd0031f62))
* add method for sending `VideoStreamMessage` response models ([8798d73](https://github.com/mahyarmirrashed/fiducial-tracker/commit/8798d737f5cd762c3e39f7c5e71eda7def70cc34))
* implement response model for `VideoStreamMessage` ([c115c46](https://github.com/mahyarmirrashed/fiducial-tracker/commit/c115c4636bb35310103e856bc6e261860c2d8c55))


### Bug Fixes

* add typing on `send_video_stream` arguments ([1c08883](https://github.com/mahyarmirrashed/fiducial-tracker/commit/1c088832754669f45e7a0e5daa0b81e8787f0685))
* update port type to REQ ([9032fb3](https://github.com/mahyarmirrashed/fiducial-tracker/commit/9032fb3862ed2e25d3a9c4b0ef6835eefcbedea7))

## [0.8.0](https://github.com/mahyarmirrashed/fiducial-tracker/compare/0.7.0...0.8.0) (2023-02-07)


### Features

* add ability to parse corners from cli ([44ba331](https://github.com/mahyarmirrashed/fiducial-tracker/commit/44ba331aac7f7daae936ce51246c846f9bc45242))
* add corner calibrator ([e4d0c1b](https://github.com/mahyarmirrashed/fiducial-tracker/commit/e4d0c1b9cab40a667836362e8a499747cafa105b))
* add parameter to specify corners ([f26c327](https://github.com/mahyarmirrashed/fiducial-tracker/commit/f26c32785191d03e55575493e604883727400a13))
* make point type return a `Point` model ([4980f81](https://github.com/mahyarmirrashed/fiducial-tracker/commit/4980f81cb95179672976adf833bd2c54478fd187))


### Bug Fixes

* make corners mandatory in messages ([7676a08](https://github.com/mahyarmirrashed/fiducial-tracker/commit/7676a08030e08d3b763837f557df7005071c9598))

## [0.7.0](https://github.com/mahyarmirrashed/fiducial-tracker/compare/0.6.0...0.7.0) (2023-02-07)


### Features

* add ability to send fiducial locations to receivers ([c1b3230](https://github.com/mahyarmirrashed/fiducial-tracker/commit/c1b3230e8ba9a9acf3a085ab2c40871848461b7c))
* display received fiducials and their locations ([154e6ec](https://github.com/mahyarmirrashed/fiducial-tracker/commit/154e6ec1df24ceafbc011fbdd99e9eee791ec420))
* make point model public ([5bb79a7](https://github.com/mahyarmirrashed/fiducial-tracker/commit/5bb79a704fe995101293286bb03b06b8331e24cd))
* **receiver:** add ability to receive location stream requests ([9a0afbc](https://github.com/mahyarmirrashed/fiducial-tracker/commit/9a0afbc829ba02cedfe7f16ce23e123231b8c101))


### Bug Fixes

* force pydantic to validate field constraints ([7b13bd2](https://github.com/mahyarmirrashed/fiducial-tracker/commit/7b13bd2065ce198b63a3f90becdd4a388336829f))

## [0.6.0](https://github.com/mahyarmirrashed/fiducial-tracker/compare/0.5.0...0.6.0) (2023-02-06)


### Features

* add `ormsgpack` and `qoi` as messaging dependencies ([c14f53d](https://github.com/mahyarmirrashed/fiducial-tracker/commit/c14f53dda734bee11f43960d137921c08a6c8b2b))
* remove numpy ndarray extensions for pydantic ([d71cc83](https://github.com/mahyarmirrashed/fiducial-tracker/commit/d71cc83d54573ec5fc577f630fc3beea03ccc82d))


### Bug Fixes

* encode/decode numpy arrays as an extra step before packing as message ([c9fedd8](https://github.com/mahyarmirrashed/fiducial-tracker/commit/c9fedd87291d2cf87173677865a77e806d46417e))
* pass unpacked dictionary into model constructor ([efa98ac](https://github.com/mahyarmirrashed/fiducial-tracker/commit/efa98accb10b6adb7d77fcc50a088adac18b575f))
* use qoi to decode encoded frame ([628ac06](https://github.com/mahyarmirrashed/fiducial-tracker/commit/628ac06748f5a5194d54e65c90ca4889b4802071))

## [0.5.0](https://github.com/mahyarmirrashed/fiducial-tracker/compare/0.4.0...0.5.0) (2023-01-30)


### Features

* add ability to clear messages from screen ([40deae6](https://github.com/mahyarmirrashed/fiducial-tracker/commit/40deae60d67a7e47b4968bb0d8571f4c10459740))
* add ability to communicate frames from client to server ([65169e9](https://github.com/mahyarmirrashed/fiducial-tracker/commit/65169e980ae081efb7894cca1834520ccd6532a8))
* add base message model class ([ad12936](https://github.com/mahyarmirrashed/fiducial-tracker/commit/ad12936473b278a1d91f1a9540b190850f212b9f))
* add client-side communicator interface ([cd1a7f5](https://github.com/mahyarmirrashed/fiducial-tracker/commit/cd1a7f56b638441774d737242ea62bd9397b6e4c))
* add location stream message protocol format ([df0dd1d](https://github.com/mahyarmirrashed/fiducial-tracker/commit/df0dd1d79e7a73c8d5c89f1902aa615a244120e8))
* add point model with named parameters ([4f871e4](https://github.com/mahyarmirrashed/fiducial-tracker/commit/4f871e4fdabbe2da9e5da7ef7b888e2cc9768d2d))
* add server-side communicator interface ([45c05a0](https://github.com/mahyarmirrashed/fiducial-tracker/commit/45c05a0511da24b6e4287bcfeab2efa3f2b35803))
* add unique id to each client ([36f83b5](https://github.com/mahyarmirrashed/fiducial-tracker/commit/36f83b533f912f2d5eda4758f7751ab7da6339b4))
* add video stream request and response object models ([74cbac0](https://github.com/mahyarmirrashed/fiducial-tracker/commit/74cbac04b0c0201590a1bca8e77c1aea58f937df))
* allow sending frames as numpy arrays ([4916ddc](https://github.com/mahyarmirrashed/fiducial-tracker/commit/4916ddc08773e93e46164c175361e1655e40ebfd))
* convert calibrator into its own importable module ([0027489](https://github.com/mahyarmirrashed/fiducial-tracker/commit/00274892daef3393104e60054c4f9440b976b45a))
* expose needed classes to outside submodules ([d8979c5](https://github.com/mahyarmirrashed/fiducial-tracker/commit/d8979c567852ece54860414069f97e7a07786db3))
* extend pydantic to allow numpy arrays ([c6e2230](https://github.com/mahyarmirrashed/fiducial-tracker/commit/c6e2230817bca5bad7ffb08f3d5370bf689bef4c))
* make models an importable module ([4982a18](https://github.com/mahyarmirrashed/fiducial-tracker/commit/4982a180adb11f606411be7c306fe7dd37fdb69c))
* update to add real-time validation for integer ([4ade707](https://github.com/mahyarmirrashed/fiducial-tracker/commit/4ade707defb96df3364159ea0457a7af6b74859e))


### Bug Fixes

* allow `orjson` to serialize numpy arrays ([5a993f2](https://github.com/mahyarmirrashed/fiducial-tracker/commit/5a993f2464e7d59eb44719e39bb5856feff08fe1))
* make corner parameters optional ([af54ea0](https://github.com/mahyarmirrashed/fiducial-tracker/commit/af54ea0e0699eced527c35864aa5b53576437930))
* make heading parameter optional until featuer is added on server ([30be8e7](https://github.com/mahyarmirrashed/fiducial-tracker/commit/30be8e70d543827565083682bf4bf31e29f81260))
* prevent extra, unspecified fields onto class ([e79c620](https://github.com/mahyarmirrashed/fiducial-tracker/commit/e79c620a0fef152bbecb4a64b706158475a92f74))

## [0.4.0](https://github.com/mahyarmirrashed/fiducial-tracker/compare/0.3.1...0.4.0) (2023-01-25)


### Features

* add file type class for argument parsing ([d4e1d68](https://github.com/mahyarmirrashed/fiducial-tracker/commit/d4e1d68f58d276165f1755acfd06c5690157d966))
* add generator for yielding next frames of video input ([1c3183b](https://github.com/mahyarmirrashed/fiducial-tracker/commit/1c3183ba0c562631da8f0dbee63e77073ad66c30))
* add mutually exclusive argument group for video input ([cea221d](https://github.com/mahyarmirrashed/fiducial-tracker/commit/cea221da7eda24e51c25ae5927123f3153604b96))
* add shorthand fieldfor video source once arguments are parsed ([eee1060](https://github.com/mahyarmirrashed/fiducial-tracker/commit/eee1060bd9d614ddfdb7e9668f0069d528f0283c))
* add wrapper class for managing resource usage ([5c47e7f](https://github.com/mahyarmirrashed/fiducial-tracker/commit/5c47e7f9fd17507ba7c97fc93ffb213bae44f228))
* consume frames generated by video reader context ([84c285c](https://github.com/mahyarmirrashed/fiducial-tracker/commit/84c285cfcaae247ce8be9d81289661486742c917))


### Bug Fixes

* `FileType` only needs extensions (not periods) ([16ac218](https://github.com/mahyarmirrashed/fiducial-tracker/commit/16ac2188aeca10281189068e12e48a79bd41131f))
* add ability to quit program while reading frames ([e0a5f02](https://github.com/mahyarmirrashed/fiducial-tracker/commit/e0a5f02dab5f79112b0e87c5b2101f3e72583437))
* change assertion to exception clause ([5397864](https://github.com/mahyarmirrashed/fiducial-tracker/commit/5397864bc53f16a5c2a9cb92c6d9bc9e38dd6a2c))
* change type assertion to exception clause ([fe5e22c](https://github.com/mahyarmirrashed/fiducial-tracker/commit/fe5e22ce18507c536b102081c5d9330032cd5e0e))
* improve function signature types ([55bbd03](https://github.com/mahyarmirrashed/fiducial-tracker/commit/55bbd031912c50476f366e2628c8c086db0b020f))
* raise range exception ([cacb9f7](https://github.com/mahyarmirrashed/fiducial-tracker/commit/cacb9f729c2c5dceab860d951f9b894342a41109))

### [0.3.1](https://github.com/mahyarmirrashed/fiducial-tracker/compare/0.3.0...0.3.1) (2023-01-23)

## [0.3.0](https://github.com/mahyarmirrashed/fiducial-tracker/compare/0.2.0...0.3.0) (2023-01-20)


### Features

* add message dropping filter based on sending delay ([6b92a66](https://github.com/mahyarmirrashed/fiducial-tracker/commit/6b92a66d5a85c80037a9e5f56bce55b06ca77ae2))

## [0.2.0](https://github.com/mahyarmirrashed/fiducial-tracker/compare/0.1.1...0.2.0) (2023-01-20)


### Features

* add pub/sub messaging from server to receivers ([7369ca6](https://github.com/mahyarmirrashed/fiducial-tracker/commit/7369ca6a9280a5d0c6d89dc6cff0405b2a691a61))
* add random uniform message generation ([f4540b8](https://github.com/mahyarmirrashed/fiducial-tracker/commit/f4540b8ea8792baf786fb14109c3c6ea1c646161))
* export IntegerRange from module ([6481daf](https://github.com/mahyarmirrashed/fiducial-tracker/commit/6481daf59c27e9a66b212e015778913f4f32e348))
* forward collected client messages to receivers ([b5ea8a8](https://github.com/mahyarmirrashed/fiducial-tracker/commit/b5ea8a878341fd51e732624bf724ddaf091bba4f))


### Bug Fixes

* correct default publisher port ([b0ad648](https://github.com/mahyarmirrashed/fiducial-tracker/commit/b0ad64870b9eb8696d6ec79c81b8a35ade1089e4))
* set no filter on subscribed information ([9e0b0b4](https://github.com/mahyarmirrashed/fiducial-tracker/commit/9e0b0b49cb82cea486b0fe46c829e8adc300922a))

## [0.1.1](https://github.com/mahyarmirrashed/fiducial-tracker/compare/0.1.0...0.1.1) (2023-01-19)

## 0.1.0 (2023-01-19)


### Features

* add range validator for argument parsing ([5a1c620](https://github.com/mahyarmirrashed/shopping-cart-tracker/commit/5a1c62098677366f6a7cbac7296edbf8460e313e))