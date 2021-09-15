######################################################################
###                                                                ###
### Custom number validator, inherited from prompt_toolkit library ###
###                                                                ###
######################################################################

from prompt_toolkit.validation import ValidationError, Validator

class ScoreValidator(Validator):
    def validate(self, document):
        text = document.text

        if text and not text.isdigit():
            i = 0

            # Get index of first non numeric character.
            # We want to move the cursor here.
            for i, c in enumerate(text):
                if not c.isdigit():
                    break

            raise ValidationError(message='This input contains non-numeric characters',
                                  cursor_position=i)

        elif text.isdigit and (float(text) < 0 or float(text) > 100):
            raise ValidationError(message='The number must be between 0-100!', cursor_position=len(text))    
