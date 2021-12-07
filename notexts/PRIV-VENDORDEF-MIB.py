#
# PySNMP MIB module PRIV-VENDORDEF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRIV-VENDORDEF-MIB
# Produced by pysmi-1.1.3 at Tue Dec  7 14:20:40 2021
# On host fv-az42-142 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, NotificationType, ObjectIdentity, Integer32, IpAddress, Counter64, enterprises, Bits, iso, TimeTicks, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "ObjectIdentity", "Integer32", "IpAddress", "Counter64", "enterprises", "Bits", "iso", "TimeTicks", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter32", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
privateVendorOID = ModuleIdentity((1, 3, 6, 1, 4, 1, 738))
privateVendorOID.setRevisions(('2007-09-29 00:00',))
if mibBuilder.loadTexts: privateVendorOID.setLastUpdated('200709290000Z')
if mibBuilder.loadTexts: privateVendorOID.setOrganization('BATM Advanced Communication')
mibBuilder.exportSymbols("PRIV-VENDORDEF-MIB", PYSNMP_MODULE_ID=privateVendorOID, privateVendorOID=privateVendorOID)
