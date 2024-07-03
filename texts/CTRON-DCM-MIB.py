#
# PySNMP MIB module CTRON-DCM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-DCM-MIB
# Produced by pysmi-1.1.12 at Wed Jul  3 13:05:32 2024
# On host fv-az1249-950 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
ctDcm, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctDcm")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Counter64, Bits, iso, ObjectIdentity, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, MibIdentifier, TimeTicks, IpAddress, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "Bits", "iso", "ObjectIdentity", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "MibIdentifier", "TimeTicks", "IpAddress", "ModuleIdentity", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dCM = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 6, 1))
dCMMode = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 6, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dCMMode.setStatus('mandatory')
if mibBuilder.loadTexts: dCMMode.setDescription('A value which indicates whether this module supports\n            a view chassis-wide of management information, accessed\n            via chassis-ip. This MIB view is actually composed of\n            information which is distributed between modules within\n            the chassis but is able to be viewed as a collective whole.\n            When a module is in standalone mode, it only supports\n            original, module-level mibs. In distributed mode, the\n            module will operate in conjunction with other distributed\n            modules to share management information and present it to\n            management clients through the chassis ip.\n\n                0 = STANDALONE\n                1 = DISTRIBUTED\n            ')
mibBuilder.exportSymbols("CTRON-DCM-MIB", dCMMode=dCMMode, dCM=dCM)
