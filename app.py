####################################################
# IMPORTS (LOCAL) ##################################
####################################################

from Karmatek import app, db

####################################################
# RUNNING SERVER ###################################
####################################################

if (__name__ == "__main__"):
    db.create_all()
    app.run(debug=True)