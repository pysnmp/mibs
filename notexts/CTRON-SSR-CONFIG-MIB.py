#
# PySNMP MIB module CTRON-SSR-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-SSR-CONFIG-MIB
# Produced by pysmi-1.1.12 at Thu Nov 28 02:57:31 2024
# On host fv-az885-149 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
ssrMibs, = mibBuilder.importSymbols("CTRON-SSR-SMI-MIB", "ssrMibs")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, iso, IpAddress, Counter64, NotificationType, ModuleIdentity, Unsigned32, Bits, Integer32, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "iso", "IpAddress", "Counter64", "NotificationType", "ModuleIdentity", "Unsigned32", "Bits", "Integer32", "TimeTicks", "Gauge32")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
ssrConfigMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 2501, 1, 230))
ssrConfigMIB.setRevisions(('2000-07-15 00:00', '2000-02-20 00:00', '1998-08-17 00:00',))
if mibBuilder.loadTexts: ssrConfigMIB.setLastUpdated('200007150000Z')
if mibBuilder.loadTexts: ssrConfigMIB.setOrganization('Cabletron Systems, Inc')
class SSRErrorCode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("noStatus", 1), ("timeout", 2), ("networkError", 3), ("noSpace", 4), ("invalidConfig", 5), ("commandCompleted", 6), ("internalError", 7), ("tftpServerError", 8))

cfgGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 231))
cfgTransferOp = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 231, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("noop", 1), ("sendConfigToAgent", 2), ("receiveConfigFromAgent", 3), ("receiveBootlogFromAgent", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfgTransferOp.setStatus('current')
cfgManagerAddress = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 231, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfgManagerAddress.setStatus('current')
cfgFileName = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 231, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfgFileName.setStatus('current')
cfgActivateTransfer = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 231, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfgActivateTransfer.setStatus('current')
cfgTransferStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 231, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("idle", 1), ("sending", 2), ("receiving", 3), ("transferComplete", 4), ("error", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfgTransferStatus.setStatus('current')
cfgActivateFile = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 231, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfgActivateFile.setStatus('current')
cfgLastError = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 231, 7), SSRErrorCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfgLastError.setStatus('current')
cfgLastErrorReason = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 231, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfgLastErrorReason.setStatus('current')
cfgActiveImageVersion = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 231, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfgActiveImageVersion.setStatus('current')
cfgActiveImageBootLocation = MibScalar((1, 3, 6, 1, 4, 1, 52, 2501, 1, 231, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfgActiveImageBootLocation.setStatus('current')
configConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 230, 3))
configCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 230, 3, 1))
configGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 2501, 1, 230, 3, 2))
configCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 2501, 1, 230, 3, 1, 1)).setObjects(("CTRON-SSR-CONFIG-MIB", "configGroup10"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    configCompliance = configCompliance.setStatus('obsolete')
configCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 2501, 1, 230, 3, 1, 2)).setObjects(("CTRON-SSR-CONFIG-MIB", "configGroup20"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    configCompliance2 = configCompliance2.setStatus('current')
configGroup10 = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 2501, 1, 230, 3, 2, 1)).setObjects(("CTRON-SSR-CONFIG-MIB", "cfgTransferOp"), ("CTRON-SSR-CONFIG-MIB", "cfgManagerAddress"), ("CTRON-SSR-CONFIG-MIB", "cfgFileName"), ("CTRON-SSR-CONFIG-MIB", "cfgActivateTransfer"), ("CTRON-SSR-CONFIG-MIB", "cfgTransferStatus"), ("CTRON-SSR-CONFIG-MIB", "cfgActivateFile"), ("CTRON-SSR-CONFIG-MIB", "cfgLastError"), ("CTRON-SSR-CONFIG-MIB", "cfgLastErrorReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    configGroup10 = configGroup10.setStatus('deprecated')
configGroup20 = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 2501, 1, 230, 3, 2, 2)).setObjects(("CTRON-SSR-CONFIG-MIB", "cfgTransferOp"), ("CTRON-SSR-CONFIG-MIB", "cfgManagerAddress"), ("CTRON-SSR-CONFIG-MIB", "cfgFileName"), ("CTRON-SSR-CONFIG-MIB", "cfgActivateTransfer"), ("CTRON-SSR-CONFIG-MIB", "cfgTransferStatus"), ("CTRON-SSR-CONFIG-MIB", "cfgActivateFile"), ("CTRON-SSR-CONFIG-MIB", "cfgLastError"), ("CTRON-SSR-CONFIG-MIB", "cfgLastErrorReason"), ("CTRON-SSR-CONFIG-MIB", "cfgActiveImageVersion"), ("CTRON-SSR-CONFIG-MIB", "cfgActiveImageBootLocation"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    configGroup20 = configGroup20.setStatus('current')
mibBuilder.exportSymbols("CTRON-SSR-CONFIG-MIB", cfgActivateTransfer=cfgActivateTransfer, configGroups=configGroups, cfgActiveImageBootLocation=cfgActiveImageBootLocation, cfgActiveImageVersion=cfgActiveImageVersion, cfgTransferStatus=cfgTransferStatus, configCompliances=configCompliances, configCompliance=configCompliance, cfgLastError=cfgLastError, configConformance=configConformance, cfgActivateFile=cfgActivateFile, cfgFileName=cfgFileName, cfgLastErrorReason=cfgLastErrorReason, cfgGroup=cfgGroup, configGroup10=configGroup10, ssrConfigMIB=ssrConfigMIB, cfgManagerAddress=cfgManagerAddress, SSRErrorCode=SSRErrorCode, configGroup20=configGroup20, cfgTransferOp=cfgTransferOp, configCompliance2=configCompliance2, PYSNMP_MODULE_ID=ssrConfigMIB)
