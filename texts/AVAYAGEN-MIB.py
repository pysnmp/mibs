#
# PySNMP MIB module AVAYAGEN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/avaya/AVAYAGEN-MIB.mib
# Produced by pysmi-1.1.12 at Wed Oct  9 02:16:39 2024
# On host fv-az1144-128 platform Linux version 6.8.0-1014-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, NotificationType, enterprises, Unsigned32, TimeTicks, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, ObjectIdentity, Gauge32, Counter64, Bits, IpAddress, iso, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "enterprises", "Unsigned32", "TimeTicks", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "ObjectIdentity", "Gauge32", "Counter64", "Bits", "IpAddress", "iso", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
avaya = ModuleIdentity((1, 3, 6, 1, 4, 1, 6889))
avaya.setRevisions(('1904-01-27 09:00', '1902-08-15 09:00', '1902-07-28 09:00', '1901-08-09 17:00', '1901-06-21 11:55', '1900-10-15 10:45', '1900-10-15 13:05',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: avaya.setRevisionsDescriptions(('Rev 1.4.0 - Meir Deutsch.\n    adds avGatewayProducts under avayaProducts.\n    adds avGatewayMibs under avayaMibs.  \n    ', 'Rev 1.3.0 - Itai Zilbershterin.\n    adds avayaSystemStats under lsg.\n    ', 'Rev 1.2.0 - Itai Zilbershterin.\n    adds avayaEISTopology under lsg.\n    ', 'Rev 1.1.0 - Itai Zilbershterin.\n    adds products OID to those defined.\n    ', 'Rev 1.0.0 - Itai Zilbershterin.\n    Fixed the mibs placement error. Avaya Mibs\n    reside under avaya.2 and not avaya.1.\n    The MIB branch is called avayaMibs.', 'Rev 0.9.0 - Itai Zilbershterin.\n    The initial version of this MIB module. \n\n    The following Organizational top-level groups are defined:\n    lsg - Mibs of the LAN System Group (Concord & Israel).', "Rev 0.9.1 - Itai Zilbershterin.\n    Dates in Revisions changed from 'yyyymmddhhmm' to 'yymmddhhmm', to support\n    older development environments.",))
if mibBuilder.loadTexts: avaya.setLastUpdated('0401270900Z')
if mibBuilder.loadTexts: avaya.setOrganization('Avaya Inc.')
if mibBuilder.loadTexts: avaya.setContactInfo('Avaya Customer Services\n\t\t\t\tPostal: Avaya, Inc.\n\t\t\t\t        211 Mt Airy Rd.\n\t\t\t\t        Basking Ridge, NJ 07920\n\t\t\t\t        USA\n\t\t\t\tTel:    +1 908 953 6000\n\t\t\t\tWWW:    http://www.avaya.com\n\t\t\t\t')
if mibBuilder.loadTexts: avaya.setDescription('Avaya top-level OID tree.\n    This MIB module deals defines the Avaya enterprise-specific tree.\n    Development organizations within Avaya who wish to register MIBs \n    under the Avaya enterprise OID, should:\n    a. Contact the maintainer of this module, and get an organization OID and\n       group OID.\n    b. Import the definition of their Organization OID from this MIB.\n    ')
products = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1))
mibs = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2))
avGatewayProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 1, 6))
avGatewayMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 6))
lsg = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 1))
avayaEISTopology = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 1, 10))
avayaSystemStats = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 1, 11))
mibBuilder.exportSymbols("AVAYAGEN-MIB", mibs=mibs, avayaEISTopology=avayaEISTopology, avaya=avaya, avayaSystemStats=avayaSystemStats, products=products, PYSNMP_MODULE_ID=avaya, avGatewayMibs=avGatewayMibs, avGatewayProducts=avGatewayProducts, lsg=lsg)
