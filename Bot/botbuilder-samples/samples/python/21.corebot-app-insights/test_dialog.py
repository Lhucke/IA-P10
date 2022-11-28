import aiounittest
import json

from libraries.botbuilder.core import ConversationState, MemoryStorage, TurnContext
from libraries.botbuilder.core.adapters import TestAdapter
from libraries.botbuilder.dialogs import DialogSet, DialogTurnStatus

from config import DefaultConfig
from dialogs import BookingDialog, MainDialog
from booking_details import BookingDetails
from flight_booking_recognizer import FlightBookingRecognizer

booking_dialog = BookingDialog()
adapter = TestAdapter()


class MainDialogTest(aiounittest.AsyncTestCase):
    """Tests for the main dialog"""

    async def test_booking_dialog_destination(self):

        """Tests the execute_luis_query method"""
        CONFIG = DefaultConfig()
        RECOGNIZER = FlightBookingRecognizer(CONFIG)

        luis_result = BookingDetails()

        async def exec_test(turn_context: TurnContext):
            dialog_context = await dialogs.create_context(turn_context)
            results = await dialog_context.continue_dialog()
            if (results.status == DialogTurnStatus.Empty):
                dialog_context.options = luis_result
                await dialog_context.begin_dialog(main_dialog._booking_dialog_id, luis_result)

            await conv_state.save_changes(turn_context)

        conv_state = ConversationState(MemoryStorage())
        dialogs_state = conv_state.create_property("dialog-state")
        dialogs = DialogSet(dialogs_state)
        booking_dialog = BookingDialog(dialog_id="id1")
        main_dialog = MainDialog(
            FlightBookingRecognizer(DefaultConfig()), booking_dialog
        )
        dialogs.add(booking_dialog)
        adapter = TestAdapter(exec_test)
        await adapter.test('I Wanna trip', 'To what city would you like to travel?', timeout=10000)


    async def test_booking_dialog_origin(self):

        """Tests the execute_luis_query method"""
        CONFIG = DefaultConfig()
        RECOGNIZER = FlightBookingRecognizer(CONFIG)

        luis_result = BookingDetails()
        luis_result.destination = "Paris"

        async def exec_test(turn_context: TurnContext):
            dialog_context = await dialogs.create_context(turn_context)
            results = await dialog_context.continue_dialog()
            if (results.status == DialogTurnStatus.Empty):
                dialog_context.options = luis_result
                await dialog_context.begin_dialog(main_dialog._booking_dialog_id, luis_result)

            await conv_state.save_changes(turn_context)

        conv_state = ConversationState(MemoryStorage())
        dialogs_state = conv_state.create_property("dialog-state")
        dialogs = DialogSet(dialogs_state)
        booking_dialog = BookingDialog(dialog_id="id1")
        main_dialog = MainDialog(
            FlightBookingRecognizer(DefaultConfig()), booking_dialog
        )
        dialogs.add(booking_dialog)
        adapter = TestAdapter(exec_test)
        await adapter.test('Paris', 'From what city will you be travelling?', timeout=10000)


    async def test_booking_dialog_travel_date(self):

        """Tests the execute_luis_query method"""
        CONFIG = DefaultConfig()
        RECOGNIZER = FlightBookingRecognizer(CONFIG)

        luis_result = BookingDetails()
        luis_result.destination = "Paris"
        luis_result.origin = "Berlin"

        async def exec_test(turn_context: TurnContext):
            dialog_context = await dialogs.create_context(turn_context)
            results = await dialog_context.continue_dialog()
            if (results.status == DialogTurnStatus.Empty):
                dialog_context.options = luis_result
                await dialog_context.begin_dialog(main_dialog._booking_dialog_id, luis_result)

            await conv_state.save_changes(turn_context)

        conv_state = ConversationState(MemoryStorage())
        dialogs_state = conv_state.create_property("dialog-state")
        dialogs = DialogSet(dialogs_state)
        booking_dialog = BookingDialog(dialog_id="id1")
        main_dialog = MainDialog(
            FlightBookingRecognizer(DefaultConfig()), booking_dialog
        )
        dialogs.add(booking_dialog)
        adapter = TestAdapter(exec_test)
        await adapter.test('Berlin', 'On what date would you like to travel?', timeout=10000)


    async def test_booking_dialog_return_date(self):

        """Tests the execute_luis_query method"""
        CONFIG = DefaultConfig()
        RECOGNIZER = FlightBookingRecognizer(CONFIG)

        luis_result = BookingDetails()
        luis_result.destination = "Paris"
        luis_result.origin = "Berlin"
        luis_result.travel_date = "12th september"

        async def exec_test(turn_context: TurnContext):
            dialog_context = await dialogs.create_context(turn_context)
            results = await dialog_context.continue_dialog()
            if (results.status == DialogTurnStatus.Empty):
                dialog_context.options = luis_result
                await dialog_context.begin_dialog(main_dialog._booking_dialog_id, luis_result)

            await conv_state.save_changes(turn_context)

        conv_state = ConversationState(MemoryStorage())
        dialogs_state = conv_state.create_property("dialog-state")
        dialogs = DialogSet(dialogs_state)
        booking_dialog = BookingDialog(dialog_id="id1")
        main_dialog = MainDialog(
            FlightBookingRecognizer(DefaultConfig()), booking_dialog
        )
        dialogs.add(booking_dialog)
        adapter = TestAdapter(exec_test)
        await adapter.test('12th september', 'On what date would you like to come back?', timeout=10000)


    async def test_booking_dialog_budget(self):

        """Tests the execute_luis_query method"""
        CONFIG = DefaultConfig()
        RECOGNIZER = FlightBookingRecognizer(CONFIG)

        luis_result = BookingDetails()
        luis_result.destination = "Paris"
        luis_result.origin = "Berlin"
        luis_result.travel_date = "12th september"
        luis_result.return_date = "12th october"

        async def exec_test(turn_context: TurnContext):
            dialog_context = await dialogs.create_context(turn_context)
            results = await dialog_context.continue_dialog()
            if (results.status == DialogTurnStatus.Empty):
                dialog_context.options = luis_result
                await dialog_context.begin_dialog(main_dialog._booking_dialog_id, luis_result)

            await conv_state.save_changes(turn_context)

        conv_state = ConversationState(MemoryStorage())
        dialogs_state = conv_state.create_property("dialog-state")
        dialogs = DialogSet(dialogs_state)
        booking_dialog = BookingDialog(dialog_id="id1")
        main_dialog = MainDialog(
            FlightBookingRecognizer(DefaultConfig()), booking_dialog
        )
        dialogs.add(booking_dialog)
        adapter = TestAdapter(exec_test)
        await adapter.test('12th october', 'What is your maximum budget?', timeout=10000)