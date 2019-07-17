# atd-gridsmart

The code in this repo is intended for the automation of tasks for our gridsmart cameras, including software updates, health status checks, etc.

# Development 

The knack application will require four enviroment variables:

- `GS_KNACK_FIELD_ID` - The field id is the internal name of a field, for instance if the field name is `DETECTOR_IP`, click on it and the URL in your browser will show the field_id. It looks like `field_1234`.
- `GS_KNACK_OBJECT_ID` - The object id is the internal name of a table. You should be able to get it the same way by clicking on the table and checking your browser's URL. The format looks like `object_1234`
- `GS_KNACK_APP_ID` - The app id, you get it through Knack -> Application -> Settings (Cog icon) -> API & Code. 
- `GS_KNACK_API_KEY` - The app id, you get it through Knack -> Application -> Settings (Cog icon) -> API & Code.

Once you have these environment settings you will be able to run the knack application.

### Environment Variables in Windows

Run a lines like these in the command prompt (examples, not real objects or api keys):

```bash
setx GS_KNACK_FIELD_ID="field_1234"
setx GS_KNACK_OBJECT_ID="object_123"
setx GS_KNACK_APP_ID="i7AoMLn88jKLwo85t39vi843jKYW54e"
setx GS_KNACK_API_KEY="fKL1a2b3c4-5d6f-7a8b-9c0d1e2f3a4b"
```

### Environment Variables in Mac/Linux

Run a lines like these in the terminal (examples, not real objects or api keys):

```bash
export GS_KNACK_FIELD_ID="field_1234"
export GS_KNACK_OBJECT_ID="object_123"
export GS_KNACK_APP_ID="i7AoMLn88jKLwo85t39vi843jKYW54e"
export GS_KNACK_API_KEY="fKL1a2b3c4-5d6f-7a8b-9c0d1e2f3a4b"
```

