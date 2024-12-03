#
# PySNMP MIB module CTRON-DCM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-DCM-MIB
# Produced by pysmi-1.1.12 at Tue Dec  3 09:42:11 2024
# On host fv-az566-8 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ctDcm, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctDcm")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Counter64, iso, TimeTicks, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Bits, ModuleIdentity, Gauge32, IpAddress, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter64", "iso", "TimeTicks", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Bits", "ModuleIdentity", "Gauge32", "IpAddress", "Unsigned32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dCM = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 6, 1))
dCMMode = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 6, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dCMMode.setStatus('mandatory')
if mibBuilder.loadTexts: dCMMode.setDescription('A value which indicates whether this module supports\n            a view chassis-wide of management information, accessed\n            via chassis-ip. This MIB view is actually composed of\n            information which is distributed between modules within\n            the chassis but is able to be viewed as a collective whole.\n            When a module is in standalone mode, it only supports\n            original, module-level mibs. In distributed mode, the\n            module will operate in conjunction with other distributed\n            modules to share management information and present it to\n            management clients through the chassis ip.\n\n                0 = STANDALONE\n                1 = DISTRIBUTED\n            ')
mibBuilder.exportSymbols("CTRON-DCM-MIB", dCMMode=dCMMode, dCM=dCM)
