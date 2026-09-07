#
# PySNMP MIB module CISCOSB-SECSD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCOSB-SECSD-MIB
# Source digest sha256:918d77f99c283d34ca6b237f9a11400fbbf369964a0eae652c1d514d47548b8e
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, RowStatus, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TruthValue")
rlSecSd = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209))
rlSecSd.setRevisions(('2011-08-31 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlSecSd.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rlSecSd.setLastUpdated('2011-08-31 00:00')
if mibBuilder.loadTexts: rlSecSd.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: rlSecSd.setContactInfo('Postal: 170 West Tasman Drive\n          San Jose , CA 95134-1706\n          USA\n\n          \n          Website:  Cisco Small Business Support Community <http://www.cisco.com/go/smallbizsupport>')
if mibBuilder.loadTexts: rlSecSd.setDescription('The private MIB module definition for Security Sensitive Data (SSD),\n                  contains the MIB tables and scalars to manage the access through\n                  the different management channels as CLI, WEB and others,\n                  for sensitive data as user names and passwords in system.')
class RlSecSdRuleUserType(TextualConvention, Integer32):
    description = 'The Security Sensitive Data channels access users.\n         user-name      - the rule is per rlSecSdRuleUserName.\n         default-user   - the rule is per the default system user name.\n         all-users      - all users which their user level permission is less then 15.\n         level-15-users - users which their user level permission is 15.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("user-name", 1), ("default-user", 2), ("level-15-users", 3), ("all-users", 4))

class RlSecSdChannelType(TextualConvention, Integer32):
    description = 'The Security Sensitive Data channels:\n         secure            - secure channels as console, ssh, scp, https.\n         insecure          - insecure channels as telnet, http.\n         secure-xml-snmp   - SNMPv3 with privacy or XML over https.\n         insecure-xml-snmp - SNMPv1/v2/v3 without privacy, xml over http.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("secure-xml-snmp", 1), ("secure", 2), ("insecure", 3), ("insecure-xml-snmp", 4))

class RlSecSdAccessType(TextualConvention, Integer32):
    description = 'The Security Sensitive Data channels default read/write access action:\n         exclude           - Security Sensitive Data can not retrieved/set.\n         include-encrypted - SSD can retrieved/set as encrypted only.\n         include-decrypted - SSD can retrieved/set as decrypted only.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("exclude", 1), ("include-encrypted", 2), ("include-decrypted", 3))

class RlSecSdPermitAccessType(TextualConvention, Integer32):
    description = 'The Security Sensitive Data channels access permit read/write action:\n         exclude           - Security Sensitive Data can not retrieved/set.\n         include-encrypted - SSD can retrieved/set as encrypted only.\n         include-decrypted - SSD can retrieved/set as decrypted only.\n         include-all       - SSD can retrieved/set as encrypted or as decrypted.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("exclude", 1), ("include-encrypted", 2), ("include-decrypted", 3), ("include-all", 4))

class RlSecSdSessionAccessType(TextualConvention, Integer32):
    description = 'The Security Sensitive Data (SSD) channels access per session:\n         exclude           - Security Sensitive Data can not retrieved.\n         include-encrypted - SSD can retrieved as encrypted only.\n         include-decrypted - SSD can retrieved as decrypted only.\n         default           - Set to the default SSD access as defined by the SSD rules.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("exclude", 1), ("include-encrypted", 2), ("include-decrypted", 3), ("default", 4))

class RlSecSdRuleOwnerType(TextualConvention, Integer32):
    description = 'The Security Sensitive Data rule owner:\n         default - default rule which is defined by the device.\n         user    - rule which is defined by user.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("default", 1), ("user", 2))

rlSecSdRulesTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlSecSdRulesTable.setStatus('current')
if mibBuilder.loadTexts: rlSecSdRulesTable.setDescription('The table holding the Security Sensitive Data access rules per:\n            user name / user level and management channel.\n            Allow to add/edit/remove Security Sensitive Data rules.')
rlSecSdRulesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCOSB-SECSD-MIB", "rlSecSdRuleUser"), (0, "CISCOSB-SECSD-MIB", "rlSecSdRuleUserName"), (0, "CISCOSB-SECSD-MIB", "rlSecSdRuleChannel"))
if mibBuilder.loadTexts: rlSecSdRulesEntry.setStatus('current')
if mibBuilder.loadTexts: rlSecSdRulesEntry.setDescription('An entry in the rlSecSdRulesTable.')
rlSecSdRuleUser = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209, 1, 1, 1), RlSecSdRuleUserType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecSdRuleUser.setStatus('current')
if mibBuilder.loadTexts: rlSecSdRuleUser.setDescription('Contains the Rule user type as described in RlSecSdRuleUserType.')
rlSecSdRuleUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 39))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecSdRuleUserName.setStatus('current')
if mibBuilder.loadTexts: rlSecSdRuleUserName.setDescription('Contains the Rule user name when rlSecSdRuleUser value is user-name,\n                     Otherwise it contains an empty string')
rlSecSdRuleChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209, 1, 1, 3), RlSecSdChannelType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecSdRuleChannel.setStatus('current')
if mibBuilder.loadTexts: rlSecSdRuleChannel.setDescription('Contains the Rule management channel type as described in RlSecSdChannelType.\n            secure-xml-snmp and insecure-xml-snmp management channels have no include-encrypted capability\n            thus their rlSecSdRulePermitRead and rlSecSdRuleRead can have only RlSecSdAccessType values of\n            exclude or include-decrypted.')
rlSecSdRuleRead = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209, 1, 1, 4), RlSecSdAccessType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecSdRuleRead.setStatus('current')
if mibBuilder.loadTexts: rlSecSdRuleRead.setDescription('Contains the Rule default read access level as described in RlSecSdAccessType,\n            must be lower or equal access from rlSecSdRulePermitRead')
rlSecSdRulePermitRead = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209, 1, 1, 5), RlSecSdPermitAccessType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecSdRulePermitRead.setStatus('current')
if mibBuilder.loadTexts: rlSecSdRulePermitRead.setDescription('Contains the Rule maximum permission access level as described in RlSecSdPermitAccessType.')
rlSecSdRuleIsDefault = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209, 1, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSecSdRuleIsDefault.setStatus('current')
if mibBuilder.loadTexts: rlSecSdRuleIsDefault.setDescription('true  - Rule has created by the by the system.\n             false - Rule has created by the user.')
rlSecSdRuleOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209, 1, 1, 7), RlSecSdRuleOwnerType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecSdRuleOwner.setStatus('current')
if mibBuilder.loadTexts: rlSecSdRuleOwner.setDescription('Contains the current Rule ownership as defined in RlSecSdRuleOwnerType.\n            when rlSecSdRuleIsDefault is true, rlSecSdRuleOwner allowed to change\n            default rule to user rule and vice versa.')
rlSecSdRuleStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209, 1, 1, 8), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecSdRuleStatus.setStatus('current')
if mibBuilder.loadTexts: rlSecSdRuleStatus.setDescription('The status of a table entry.\n            It is used to Add/Edit/Delete an entry from this table.')
rlSecSdMngSessionsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: rlSecSdMngSessionsTable.setStatus('current')
if mibBuilder.loadTexts: rlSecSdMngSessionsTable.setDescription('The table holding Security Sensitive Data management sessions.\n            Allowing to get management channel, user name, user level.')
rlSecSdMngSessionsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209, 2, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCOSB-SECSD-MIB", "rlSecSdMngSessionId"))
if mibBuilder.loadTexts: rlSecSdMngSessionsEntry.setStatus('current')
if mibBuilder.loadTexts: rlSecSdMngSessionsEntry.setDescription('An entry in the rlSecSdMngSessionsTable.')
rlSecSdMngSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSecSdMngSessionId.setStatus('current')
if mibBuilder.loadTexts: rlSecSdMngSessionId.setDescription('Contains the Security Sensitive Data management session identifier,\n             rlSecSdCurrentSessionId is used to get the current management session identifier')
rlSecSdMngSessionUserLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSecSdMngSessionUserLevel.setStatus('current')
if mibBuilder.loadTexts: rlSecSdMngSessionUserLevel.setDescription('Contains the Security Sensitive Data management session user access level.')
rlSecSdMngSessionUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 160))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecSdMngSessionUserName.setStatus('current')
if mibBuilder.loadTexts: rlSecSdMngSessionUserName.setDescription('Contains the Security Sensitive Data management session user name.')
rlSecSdMngSessionChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209, 2, 1, 4), RlSecSdChannelType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSecSdMngSessionChannel.setStatus('current')
if mibBuilder.loadTexts: rlSecSdMngSessionChannel.setDescription('Contains the Security Sensitive Data management session channel type as described in RlSecSdChannelType.')
rlSecSdSessionControl = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209, 3), RlSecSdSessionAccessType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecSdSessionControl.setStatus('current')
if mibBuilder.loadTexts: rlSecSdSessionControl.setDescription('Action scalar which set the default read access of Security Sensitive Data.\n            Affect only on session which from this scalar is configured.\n            Scalar Get value is the default-display/read of the session which from\n            this scalar is retrieved.')
rlSecSdCurrentSessionId = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSecSdCurrentSessionId.setStatus('current')
if mibBuilder.loadTexts: rlSecSdCurrentSessionId.setDescription('Get the current SSD management channel identifier,\n            used to get information from rlSecSdMngSessionsTable.')
rlSecSdPassPhrase = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 160)).clone('')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecSdPassPhrase.setStatus('current')
if mibBuilder.loadTexts: rlSecSdPassPhrase.setDescription('Set the passphrase for the SSD encryptyption / decryption key.\n             on set, passphrase is in plain text format.\n             on get, passphrase is encrypted.')
rlSecSdFilePassphraseControl = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("restricted", 1), ("unrestricted", 2))).clone('unrestricted')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecSdFilePassphraseControl.setStatus('current')
if mibBuilder.loadTexts: rlSecSdFilePassphraseControl.setDescription('File Passphrase control provides an additional level of protection on passphrase and configurations.\n            restricted - a device restricts its passphrase from being inserted into a configuration file.\n            unrestricted - (default) a device will include its passphrase when creating a configuration file.')
rlSecSdFileIntegrityControl = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecSdFileIntegrityControl.setStatus('current')
if mibBuilder.loadTexts: rlSecSdFileIntegrityControl.setDescription('File integrity control provides a validation of configuration file.\n            enable - Validate the configuration file digest when downloading the file to startup configuration.\n            disable - Do not validate.')
rlSecSdConfigurationFileSsdDigest = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 160)).clone('')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecSdConfigurationFileSsdDigest.setStatus('current')
if mibBuilder.loadTexts: rlSecSdConfigurationFileSsdDigest.setDescription('SSD block in configuration file integrity digest, auxiliary action scalar for\n             internal system using during configuration download.')
rlSecSdConfigurationFileDigest = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 160)).clone('')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecSdConfigurationFileDigest.setStatus('current')
if mibBuilder.loadTexts: rlSecSdConfigurationFileDigest.setDescription('SSD configuration file integrity digest, auxiliary action scalar for\n             internal system using during configuration download.')
rlSecSdFileIndicator = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 209, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 39))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSecSdFileIndicator.setStatus('current')
if mibBuilder.loadTexts: rlSecSdFileIndicator.setDescription('Retrieve configuration file SSD indicator.\n             set value: configuration file name.\n             get value: Exclude, Encrypted, Plaintext')
mibBuilder.exportSymbols("CISCOSB-SECSD-MIB", PYSNMP_MODULE_ID=rlSecSd, RlSecSdAccessType=RlSecSdAccessType, RlSecSdChannelType=RlSecSdChannelType, RlSecSdPermitAccessType=RlSecSdPermitAccessType, RlSecSdRuleOwnerType=RlSecSdRuleOwnerType, RlSecSdRuleUserType=RlSecSdRuleUserType, RlSecSdSessionAccessType=RlSecSdSessionAccessType, rlSecSd=rlSecSd, rlSecSdConfigurationFileDigest=rlSecSdConfigurationFileDigest, rlSecSdConfigurationFileSsdDigest=rlSecSdConfigurationFileSsdDigest, rlSecSdCurrentSessionId=rlSecSdCurrentSessionId, rlSecSdFileIndicator=rlSecSdFileIndicator, rlSecSdFileIntegrityControl=rlSecSdFileIntegrityControl, rlSecSdFilePassphraseControl=rlSecSdFilePassphraseControl, rlSecSdMngSessionChannel=rlSecSdMngSessionChannel, rlSecSdMngSessionId=rlSecSdMngSessionId, rlSecSdMngSessionUserLevel=rlSecSdMngSessionUserLevel, rlSecSdMngSessionUserName=rlSecSdMngSessionUserName, rlSecSdMngSessionsEntry=rlSecSdMngSessionsEntry, rlSecSdMngSessionsTable=rlSecSdMngSessionsTable, rlSecSdPassPhrase=rlSecSdPassPhrase, rlSecSdRuleChannel=rlSecSdRuleChannel, rlSecSdRuleIsDefault=rlSecSdRuleIsDefault, rlSecSdRuleOwner=rlSecSdRuleOwner, rlSecSdRulePermitRead=rlSecSdRulePermitRead, rlSecSdRuleRead=rlSecSdRuleRead, rlSecSdRuleStatus=rlSecSdRuleStatus, rlSecSdRuleUser=rlSecSdRuleUser, rlSecSdRuleUserName=rlSecSdRuleUserName, rlSecSdRulesEntry=rlSecSdRulesEntry, rlSecSdRulesTable=rlSecSdRulesTable, rlSecSdSessionControl=rlSecSdSessionControl)
