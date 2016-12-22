from kivy.app import App
from jnius import autoclass
from kivy.properties import NumericProperty

currentActivity = autoclass("org.renpy.android.PythonActivity").mActivity
#System = autoclass("android.provider.Settings$Global")
System = autoclass("android.provider.Settings$System")


class BrightApp(App):
    curr_brightness = NumericProperty(175)

    def set_android_brightness(self, upordown):
        print upordown
        if upordown == "raise":
            self.curr_brightness += 10
        else:
            self.curr_brightness -= 10

        # You need to check if it is in automatic mode first, I think
        # You need to use getContentResolver from mainactivity
        # Refer to https://developer.android.com/reference/android/provider/Settings.System.html
        # for more information on using the System settings.
        # The application wil crash if you go above 255 brightness, or below 0.
        # You will also have issues if it is set in automatic brightness mode,
        # So you should check for that first.
        print System.ADB_ENABLED, "===ADB ENABLED"
        print System.getInt(currentActivity.getContentResolver(),
                            System.SCREEN_BRIGHTNESS), "== CURRENT BRIGHTNESS"
        System.putInt(currentActivity.getContentResolver(),
                      System.SCREEN_BRIGHTNESS, self.curr_brightness)


if __name__ == "__main__":
    BrightApp().run()
