#
# PySNMP MIB module EdgeSwitch-REF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/edgeswitch/EdgeSwitch-REF-MIB
# Produced by pysmi-1.1.12 at Tue Dec  3 12:34:13 2024
# On host fv-az658-333 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, Integer32, ObjectIdentity, NotificationType, TimeTicks, Gauge32, enterprises, MibIdentifier, Counter32, ModuleIdentity, Unsigned32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "Integer32", "ObjectIdentity", "NotificationType", "TimeTicks", "Gauge32", "enterprises", "MibIdentifier", "Counter32", "ModuleIdentity", "Unsigned32", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
broadcom = ModuleIdentity((1, 3, 6, 1, 4, 1, 4413))
broadcom.setRevisions(('2007-05-23 00:00', '2003-11-21 00:00', '2003-02-06 12:00',))
if mibBuilder.loadTexts: broadcom.setLastUpdated('200705230000Z')
if mibBuilder.loadTexts: broadcom.setOrganization('Broadcom Inc')
broadcomProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1))
fastPath = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1))
class AgentPortMask(TextualConvention, OctetString):
    status = 'current'

mibBuilder.exportSymbols("EdgeSwitch-REF-MIB", broadcom=broadcom, PYSNMP_MODULE_ID=broadcom, fastPath=fastPath, AgentPortMask=AgentPortMask, broadcomProducts=broadcomProducts)
