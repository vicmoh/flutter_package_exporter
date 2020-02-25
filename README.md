# About

Creates an export dart file which exports all
the files under the `src` folder.

# Installation

To install this, git clone this repo under the `lib`
folder on your Flutter packages. All packages must be
under the `src` folder to have the widgets listed and exported.

For example:

```
lib/
   |-> src/ Your files to be package and exported.
   |-> git clone here!
```

# How to run

If you don't have `make` installed, you can
install using `brew` if you are on MacOS.
Type `brew install make` to install `make`.

To run and create export file type `make FILE='your_export_name'`.

# Example output

For example typing `make FILE=flutter_components`,
the script will find all widgets that needs to be exported.
It outputs a `flutter_components.dart` file containing 
all exported widgets. 

Example below of the `flutter_components.dart`:

```dart
library flutter_components;

export './src/independent/shape/solid_circle.dart';
export './src/independent/shape/solid_circle.dart.dart';
export './src/independent/list_items/comment_tile.dart';
export './src/independent/list_items/chat_bubble.dart';
export './src/independent/list_items/custom_tile.dart';
export './src/independent/clickables/custom_button.dart';
export './src/independent/labels/expandable_text.dart';
export './src/independent/labels/marquee_widget.dart';
export './src/independent/labels/icon_text.dart';
export './src/independent/labels/marquee_text.dart';
export './src/independent/gesture/hide_keyboard_gesture.dart';
export './src/independent/gesture/scroll_detector.dart';
export './src/independent/dialogs/full_screen_popup_view.dart';
export './src/independent/dialogs/custom_dialog.dart';
export './src/independent/alignments/vertical_stretch.dart';
export './src/independent/alignments/horizontal_stretch.dart';
export './src/independent/alignments/center_list_view.dart';
export './src/independent/animations/animate.dart';
export './src/independent/widgets/vertical_shadows.dart';
export './src/independent/widgets/backdrop_scaffold.dart';
export './src/independent/widgets/stack_avatars.dart';
export './src/independent/widgets/frosted_glass.dart';
export './src/independent/widgets/icon_shadow.dart';
export './src/independent/inputs/custom_field.dart';
export './src/independent/inputs/message_field.dart';
export './src/independent/inputs/phone_number_field.dart';
export './src/schmick/schmick_post_card_skeleton.dart';
export './src/transitions/page_transitions.dart';
export './src/transitions/transparent_page_route.dart';
```