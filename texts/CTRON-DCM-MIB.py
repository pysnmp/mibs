#
# PySNMP MIB module CTRON-DCM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-DCM-MIB
# Produced by pysmi-1.1.8 at Thu Oct 12 08:17:50 2023
# On host fv-az585-225 platform Linux version 6.2.0-1012-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ctDcm, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctDcm")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, MibIdentifier, iso, TimeTicks, NotificationType, Counter32, Counter64, ModuleIdentity, IpAddress, Integer32, Bits, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "MibIdentifier", "iso", "TimeTicks", "NotificationType", "Counter32", "Counter64", "ModuleIdentity", "IpAddress", "Integer32", "Bits", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dCM = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 6, 1))
dCMMode = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 6, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dCMMode.setStatus('mandatory')
if mibBuilder.loadTexts: dCMMode.setDescription('A value which indicates whether this module supports\n            a view chassis-wide of management information, accessed\n            via chassis-ip. This MIB view is actually composed of\n            information which is distributed between modules within\n            the chassis but is able to be viewed as a collective whole.\n            When a module is in standalone mode, it only supports\n            original, module-level mibs. In distributed mode, the\n            module will operate in conjunction with other distributed\n            modules to share management information and present it to\n            management clients through the chassis ip.\n\n                0 = STANDALONE\n                1 = DISTRIBUTED\n            ')
mibBuilder.exportSymbols("CTRON-DCM-MIB", dCM=dCM, dCMMode=dCMMode)
