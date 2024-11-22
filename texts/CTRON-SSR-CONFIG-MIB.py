#
# PySNMP MIB module CTRON-SSR-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-SSR-CONFIG-MIB
# Produced by pysmi-1.1.12 at Fri Nov 22 15:38:59 2024
# On host fv-az973-242 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ssrMibs, = mibBuilder.importSymbols("CTRON-SSR-SMI-MIB", "ssrMibs")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, IpAddress, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Gauge32, Integer32, Counter32, ObjectIdentity, NotificationType, Counter64, MibIdentifier, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "IpAddress", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Gauge32", "Integer32", "Counter32", "ObjectIdentity", "NotificationType", "Counter64", "MibIdentifier", "iso")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ssrConfigMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 2501, 1, 230))
ssrConfigMIB.setRevisions(('2000-07-15 00:00', '2000-02-20 00:00', '1998-08-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ssrConfigMIB.setRevisionsDescriptions(('Revision #3. Update contact information for Enterasys Networks as this mib\n          is found on the Riverstione RS product line as well as Enterasys SSR product line.', 'Revision #2. add two objects to obtain current prom and firmware version.', 'Revision #1. Provide startup configuration file retrieval, \n          startup log and append new commands.',))
if mibBuilder.loadTexts: ssrConfigMIB.setLastUpdated('200007150000Z')
if mibBuilder.loadTexts: ssrConfigMIB.setOrganization('Cabletron Systems, Inc')
if mibBuilder.loadTexts: ssrConfigMIB.setContactInfo('Enterasys Networks\n     35 Industrial Way, P.O. Box 5005\n     Rochester, NH 03867-0505\n     (603) 332-9400\n     support@enterasys.com\n     http://www.enterasys.com')
if mibBuilder.loadTexts: ssrConfigMIB.setDescription('This mib module defines an SNMP API to manage SmartSwitch \n          Router configuration files and system images')
class SSRErrorCode(TextualConvention, Integer32):
    description = 'A unique value, greater than zero defining the operation\n         completion status.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("noStatus", 1), ("timeout", 2), ("networkError", 3), ("noSpace", 4), ("invalidConfig", 5), ("commandCompleted", 6), ("internalError", 7), ("tftpServerError", 8))

cfgGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 231))
cfgTransferOp = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 231, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("noop", 1), ("sendConfigToAgent", 2), ("receiveConfigFromAgent", 3), ("receiveBootlogFromAgent", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfgTransferOp.setStatus('current')
if mibBuilder.loadTexts: cfgTransferOp.setDescription('Tranfer operation to be performed. Configuration\n        files are ASCII NVT text files describing the operation of the shelf.\n        Send operations use tftp to transfer a file from the manager to agent.\n        Receive operations use tftp to transfer the file from the agent to the \n        manager. Default value is no operation or noop.')
cfgManagerAddress = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 231, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfgManagerAddress.setStatus('current')
if mibBuilder.loadTexts: cfgManagerAddress.setDescription('The IPv4 address of the Manager to be used by the agent for\n         for cfgTransferOp operations. Default value is 0.0.0.0. Address must be \n         a unicast address that is reachable from the agent and no firewalls/acls \n         preventing tftp datagrams from being transferred.')
cfgFileName = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 231, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfgFileName.setStatus('current')
if mibBuilder.loadTexts: cfgFileName.setDescription('The file name to be retrieved from the tftp server at \n         host cfgManagerAddress or to be written to. Default value is blank. \n         Length of filename string must not exceed 255 alpha-numeric characters, \n         no spaces in filenames.')
cfgActivateTransfer = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 231, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfgActivateTransfer.setStatus('current')
if mibBuilder.loadTexts: cfgActivateTransfer.setDescription('Activate the file transfer operation with a value of True(1) or \n         stop it with False(2). Poll cfgTransferStatus for current status. \n        Default value is False. cfgFileName, cfgManagerAddress and cfgTransferOp\n        must be valid prior to setting this object to True. This object is equivalent to\n        the CLI command: copy tftp-server to startup if cfgRequestOp == sendConfig')
cfgTransferStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 231, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("idle", 1), ("sending", 2), ("receiving", 3), ("transferComplete", 4), ("error", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfgTransferStatus.setStatus('current')
if mibBuilder.loadTexts: cfgTransferStatus.setDescription('The current status of the transfer task. Default state is idle. \n         sending indicates a file transfer (agent->mgr) in progress. \n         receiving indicates sending a file from Manager to agent. \n         transferComplete indicates a successful transfer. error indicates\n         a failed transfer. See cfgLastError to diagnose why the transfer failed.')
cfgActivateFile = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 231, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfgActivateFile.setStatus('current')
if mibBuilder.loadTexts: cfgActivateFile.setDescription('Once a transfer to the SmartSwitchRouter is complete, Set this object\n         to True to activate the new configuration.\n         If activateConfigFile operation was successful, this object performs\n         the CLI equivalent to these commands: negate all existing commands,\n         copy scratchpad to active, copy scratchpad to startup')
cfgLastError = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 231, 7), SSRErrorCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfgLastError.setStatus('current')
if mibBuilder.loadTexts: cfgLastError.setDescription('A reason code for the last transfer operation. Poll this value\n         when doing sets against cfgMakeActive for config files obtain status.')
cfgLastErrorReason = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 231, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfgLastErrorReason.setStatus('current')
if mibBuilder.loadTexts: cfgLastErrorReason.setDescription('A string representation of cfgLastError which may contain addtional details.')
cfgActiveImageVersion = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 231, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfgActiveImageVersion.setStatus('current')
if mibBuilder.loadTexts: cfgActiveImageVersion.setDescription('The Version string of the current image executing on this control module. This\n          is the same description as the system show version command. example:  1.1.0.0')
cfgActiveImageBootLocation = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 231, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfgActiveImageBootLocation.setStatus('current')
if mibBuilder.loadTexts: cfgActiveImageBootLocation.setDescription('The URL location string from whence the current image was loaded. \n          example:  slot0:boot/ssr8.tar.gz/')
configConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 230, 3))
configCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 230, 3, 1))
configGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 230, 3, 2))
configCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 2501, 1, 230, 3, 1, 1)).setObjects(("CTRON-SSR-CONFIG-MIB", "configGroup10"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    configCompliance = configCompliance.setStatus('obsolete')
if mibBuilder.loadTexts: configCompliance.setDescription('The compliance statement for SNMP entities which implement\n            the SmartSwitch Router Config Management MIB.')
configCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 2501, 1, 230, 3, 1, 2)).setObjects(("CTRON-SSR-CONFIG-MIB", "configGroup20"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    configCompliance2 = configCompliance2.setStatus('current')
if mibBuilder.loadTexts: configCompliance2.setDescription('The compliance statement for SNMP entities which implement\n            the SmartSwitch Router Config Management MIB.')
configGroup10 = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 2501, 1, 230, 3, 2, 1)).setObjects(("CTRON-SSR-CONFIG-MIB", "cfgTransferOp"), ("CTRON-SSR-CONFIG-MIB", "cfgManagerAddress"), ("CTRON-SSR-CONFIG-MIB", "cfgFileName"), ("CTRON-SSR-CONFIG-MIB", "cfgActivateTransfer"), ("CTRON-SSR-CONFIG-MIB", "cfgTransferStatus"), ("CTRON-SSR-CONFIG-MIB", "cfgActivateFile"), ("CTRON-SSR-CONFIG-MIB", "cfgLastError"), ("CTRON-SSR-CONFIG-MIB", "cfgLastErrorReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    configGroup10 = configGroup10.setStatus('deprecated')
if mibBuilder.loadTexts: configGroup10.setDescription('The collection of objects which are used to represent version 1.0\n             file transfer operations in the SmartSwitch Router.')
configGroup20 = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 2501, 1, 230, 3, 2, 2)).setObjects(("CTRON-SSR-CONFIG-MIB", "cfgTransferOp"), ("CTRON-SSR-CONFIG-MIB", "cfgManagerAddress"), ("CTRON-SSR-CONFIG-MIB", "cfgFileName"), ("CTRON-SSR-CONFIG-MIB", "cfgActivateTransfer"), ("CTRON-SSR-CONFIG-MIB", "cfgTransferStatus"), ("CTRON-SSR-CONFIG-MIB", "cfgActivateFile"), ("CTRON-SSR-CONFIG-MIB", "cfgLastError"), ("CTRON-SSR-CONFIG-MIB", "cfgLastErrorReason"), ("CTRON-SSR-CONFIG-MIB", "cfgActiveImageVersion"), ("CTRON-SSR-CONFIG-MIB", "cfgActiveImageBootLocation"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    configGroup20 = configGroup20.setStatus('current')
if mibBuilder.loadTexts: configGroup20.setDescription('The collection of objects which are used to represent version 2.0\n             configuration operations in the SmartSwitch Router version.')
mibBuilder.exportSymbols("CTRON-SSR-CONFIG-MIB", configConformance=configConformance, cfgActiveImageBootLocation=cfgActiveImageBootLocation, configGroup20=configGroup20, cfgTransferOp=cfgTransferOp, SSRErrorCode=SSRErrorCode, cfgFileName=cfgFileName, PYSNMP_MODULE_ID=ssrConfigMIB, cfgActivateFile=cfgActivateFile, cfgLastError=cfgLastError, configCompliances=configCompliances, ssrConfigMIB=ssrConfigMIB, cfgGroup=cfgGroup, configCompliance=configCompliance, configGroup10=configGroup10, cfgManagerAddress=cfgManagerAddress, cfgActiveImageVersion=cfgActiveImageVersion, cfgActivateTransfer=cfgActivateTransfer, cfgTransferStatus=cfgTransferStatus, configGroups=configGroups, configCompliance2=configCompliance2, cfgLastErrorReason=cfgLastErrorReason)
